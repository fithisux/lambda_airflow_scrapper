from datetime import datetime
from pprint import pprint
from airflow import DAG
from airflow.decorators import task_group

from airflow.operators.python import PythonOperator
from airflow.decorators import dag

from day_four.operators.helper_operators import AWSSampleOperator2


dag = DAG(
    "scrap_lambda",
    default_args={"retries": 1},
    start_date=datetime(2021, 1, 1),
    catchup=False,
    schedule_interval="@daily",
    tags=["ote-workshop"],
)

run_this = AWSSampleOperator2(task_id="do_the_call", dag=dag)