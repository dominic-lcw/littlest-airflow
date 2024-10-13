from datetime import datetime, timedelta
from airflow import DAG

from airflow.operators.python import PythonOperator
from airflow.operators.empty import EmptyOperator

from ltaf.lib.api.binance import get_spot

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 9, 1),
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'binance_dag',
    default_args=default_args,
    description='Hit binance API and store data.',
    schedule_interval=timedelta(days=1),
    catchup = False
)

task1 = PythonOperator(
    task_id='start',
    python_callable=get_spot,
    dag=dag,
)

task2 = EmptyOperator(
    task_id='end',
    dag=dag,
)

task1 >> task2