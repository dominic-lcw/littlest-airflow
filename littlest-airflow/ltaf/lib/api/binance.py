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
            FROM binance_spot
            SELECT *, STRFTIME(CURRENT_TIMESTAMP, '%Y-%m-%d %H:%M:%S') AS snapped_time;
        """
    ))

    logging.info("Created table binance_spot")  

if __name__ == "__main__":
    print(get_spot())
