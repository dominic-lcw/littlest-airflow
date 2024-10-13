import duckdb
import logging
logging.basicConfig(level=logging.INFO)

__all__ = ['get_spot']

def get_spot():

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

    # TODO: postgres attach shall be moved to utils
    duckdb.sql(
        """
            -- sql
            INSTALL postgres;
            LOAD postgres;
            ATTACH 'dbname=postgres user=postgres password=postgres host=postgres-server port=5432' AS pg (TYPE POSTGRES, SCHEMA 'public_cache');

            -- sql
            CREATE TABLE IF NOT EXISTS pg.btc_spot AS
                SELECT * FROM binance_spot LIMIT 0;

            -- sql
            INSERT INTO pg.btc_spot 
            SELECT * FROM binance_spot;
        """
    )
    logging.info("Inserted data into postgres")



if __name__ == "__main__":
    print(get_spot())
