import boto3
import botocore
import json

def lambda_handler(event, context):
   print(f'boto3 version: {boto3.__version__}')
   print(f'botocore version: {botocore.__version__}')
   print('Lambda function triggered')
   print(f'Event: {json.dumps(event)}')
   print(f'Context:  {context.aws_request_id }')
   return "Happy Nation"