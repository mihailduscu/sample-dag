from datetime import datetime, timedelta, timezone

from airflow import DAG
from airflow.operators.python import PythonOperator


def say_hello():
    print("Hello from Airflow!")

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='hello_world_dag',
    default_args=default_args,
    description='A simple Hello World DAG',
    schedule_interval=None,  # Only triggered manually
    start_date=datetime.now(timezone.utc) - timedelta(days=1),  # timezone-aware
    catchup=False,
    tags=['example'],
) as dag:

    hello_task = PythonOperator(
        task_id='say_hello',
        python_callable=say_hello
    )

    hello_task
