from datetime import datetime

from airflow import DAG
from operators.helper_operators import AWSScrapOperator

dag = DAG(
    "call_scrap_lambda",
    default_args={"retries": 1},
    start_date=datetime(2021, 1, 1),
    catchup=False,
    schedule_interval="@daily",
    tags=["ote-workshop"],
)

run_this = AWSScrapOperator(task_id="do_the_call", dag=dag)
