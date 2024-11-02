import duckdb
import logging
logging.basicConfig(level=logging.INFO)

__all__ = ['get_spot']

# TODO: this functiono can be moved to util.
def connect(
        host: str = "localhost",
        port: int = 5432,
        user: str = "postgres",
        password: str = "postgres",
        schema: str = "public"):
    
    connection_string = f"dbname=postgres host={host} port={port} user={user} password={password} "
    duckdb.sql(
        f"""
            INSTALL postgres;
            LOAD postgres;
            ATTACH '{connection_string}' AS pg (TYPE POSTGRES, SCHEMA '{schema}');
        """
    )
    logging.info("Connected to postgres")


def get_spot(version: int = 1):

    logging.info(duckdb.sql(
        """
            -- sql
            CREATE OR REPLACE TABLE binance_spot AS
                SELECT * FROM read_json('https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT');

            -- sql
            CREATE OR REPLACE TABLE binance_spot AS
                FROM binance_spot
                SELECT *, CURRENT_TIMESTAMP AS snapped_time;
        """
    ))

    logging.info("Created table binance_spot")  

    match version:
        case 1:
            connect(host = "postgres-server", schema = "public_cache")
        case 2:
            connect(host = "postgres-duckdb-server", port = 5433, schema = "public_cache")
        case _:
            raise ValueError("Invalid version")
        
    duckdb.sql(
        """
            -- sql
            CREATE TABLE IF NOT EXISTS pg.btc_spot AS
                SELECT * FROM binance_spot LIMIT 0;

            -- sql
            DELETE FROM pg.btc_spot WHERE
                snapped_time = (SELECT MAX(snapped_time) FROM binance_spot);
                
            -- sql
            INSERT INTO pg.btc_spot (symbol, price, snapped_time)
            SELECT * FROM binance_spot;
        """
    )
    logging.info("Inserted data into postgres")



if __name__ == "__main__":
    print(get_spot())
