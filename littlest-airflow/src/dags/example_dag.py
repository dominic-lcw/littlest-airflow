from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

def example_task():
    print("This is an example task.")

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 10, 1),
    'retries': 1,
}

with DAG('example_dag',
         default_args=default_args,
         schedule_interval='@daily',
         catchup=False) as dag:

    start = DummyOperator(task_id='start')

    task1 = PythonOperator(task_id='example_task', python_callable=example_task)

    end = DummyOperator(task_id='end')

    start >> task1 >> end