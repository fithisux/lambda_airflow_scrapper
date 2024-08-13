# lambda_airflow_scrapper
(In progress, check back , will remove this when ready) A server-less scrapper that is used through airflow
An example using local stack to show airflow lambda functionality.

Code is taken (and re-written in some parts) frpm [this article](https://iwebdatascrapingservices.medium.com/how-to-scrape-news-content-from-popular-news-sites-636eea9db9a0)

## Linting

`python -m venv venv`
`venv\Scripts\activate.bat`
`pip install -r requirements-dev.txt`

and then, for linting and first ingestion

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


## Run your scrapper

`aws --endpoint-url=http://localhost:4566 lambda delete-function --function-name mysecondlambda`

`aws --endpoint-url=http://localhost:4566 lambda create-function --function-name mysecondlambda --zip-file fileb://lambda_scrapper.zip --handler lambda_scrapper.lambda_handler --runtime python3.12 --role arn:aws:iam::000000000000:role/lambda-example`

`aws --endpoint-url=http://localhost:4566 lambda invoke --function-name mysecondlambda --payload file://payload.json response.json`

## Inspect mongo

`docker exec -it lambda_airflow_scrapper-mongo-1 mongosh --username root --password`


The container name may differ, find through `docker ps`. Password is **example**.

Now to inspect

`use scrap_db`
`db.scrap_col.find({})`.

## Airflow

Enter

`c:\work\lambda_airflow_scrapper\astronomer-with-lambda`

and execute

`c:\tools\astro_1.29.0_windows_amd64.exe dev start`

install again the scrapper

`aws --endpoint-url=http://localhost:4566 iam create-role --role-name lambda-example --assume-role-policy-document file://trust-policy.json`

`aws --endpoint-url=http://localhost:4566 lambda delete-function --function-name mysecondlambda`

`aws --endpoint-url=http://localhost:4566 lambda create-function --function-name mysecondlambda --zip-file fileb://lambda_scrapper.zip --handler lambda_scrapper.lambda_handler --runtime python3.12 --role arn:aws:iam::000000000000:role/lambda-example`

and run the DAG.

Inspect as before

`docker exec -it astronomer-with-lambda_46ea20-mongo-1 mongosh --username root --passworddocker exec -it lambda_airflow_scrapper-mongo-1 mongosh --username root --password`

The container name may differ, find through `docker ps`. Password is **example**.
