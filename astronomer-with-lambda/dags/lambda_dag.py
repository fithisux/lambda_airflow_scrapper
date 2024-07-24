from datetime import datetime

from airflow import DAG
from day_four.operators.helper_operators import AWSSampleOperator1

dag = DAG(
    "call_scrap_lambda",
    default_args={"retries": 1},
    start_date=datetime(2021, 1, 1),
    catchup=False,
    schedule_interval="@daily",
    tags=["ote-workshop"],
)

run_this = AWSSampleOperator1(task_id="do_the_call", dag=dag)
