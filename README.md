# lambda_airflow_scrapper
(In progress, check back , will remove this when ready) A server-less scrapper that is used through airflow
An example using local stack to show airflow lambda functionality.

Code is taken (and re-written in some parts) frpm [this article](https://iwebdatascrapingservices.medium.com/how-to-scrape-news-content-from-popular-news-sites-636eea9db9a0)

## Liniting

`python -m venv venv`
`venv\Scripts\activate.bat`
`pip install -r requirements-dev.txt`

and then, for liniting and first ingestion

`tox run`

## Packaging

Because we will deploy to linux we need

`docker run -it --rm --name my-running-script -v C:/work/lambda_airflow_scrapper:/usr/src/myapp python:3 /usr/src/myapp/packaging`

## Run LocalStack docker container

`docker-compose up`

## Install aws-cli

https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

## Create IAM access

`aws --endpoint-url=http://localhost:4566 iam create-role --role-name lambda-example --assume-role-policy-document file://trust-policy.json`

## Delete Lambda Function

`aws --endpoint-url=http://localhost:4566 lambda delete-function --function-name myfirstlambda`

## Create Lambda function

`aws --endpoint-url=http://localhost:4566 lambda create-function --function-name myfirstlambda --zip-file fileb://my_script.zip --handler my_script.lambda_handler --runtime python3.12 --role arn:aws:iam::000000000000:role/lambda-example`

## Run yout Lambda 

`aws --endpoint-url=http://localhost:4566 lambda invoke --function-name myfirstlambda --cli-binary-format raw-in-base64-out --payload file://payload.json out --log-type Tail --query 'LogResult' --output text`


## Run your scrapper

`aws --endpoint-url=http://localhost:4566 lambda delete-function --function-name mysecondlambda`

`aws --endpoint-url=http://localhost:4566 lambda create-function --function-name mysecondlambda --zip-file fileb://lambda_scrapper.zip --handler lambda_scrapper.lambda_handler --runtime python3.12 --role arn:aws:iam::000000000000:role/lambda-example`

`aws --endpoint-url=http://localhost:4566 lambda invoke --function-name mysecondlambda --payload file://payload.json response.json`