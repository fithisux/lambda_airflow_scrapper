import json
import logging

import boto3
import pendulum
from airflow.models import BaseOperator
from airflow.models.taskinstance import Context

logger = logging.getLogger(__name__)


# https://cevo.com.au/post/revisit-airflow-lambda-operator/


class AWSSCrapOperator(BaseOperator):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def execute(self, context: Context):
        data_interval_start: pendulum.DateTime = context["data_interval_start"]
        what_time_is_it = data_interval_start.to_date_string()
        # endpoint_url = "http://localhost.localstack.cloud:4566"
        endpoint_url = "http://host.docker.internal:4566"
        client = boto3.client("lambda", endpoint_url=endpoint_url)

        response = client.invoke(
            FunctionName="mysecondlambda",
            LogType="Tail",
            ClientContext="string",
            Payload=json.dumps({"scrap_stamp": what_time_is_it}).encode("utf-8"),
        )

        logger.info(response)

        logger.info(response["Payload"].read())
