FROM quay.io/astronomer/astro-runtime:10.6.0

# install dbt into a virtual environment
RUN python -m pip install boto3

# set a connection to the airflow metadata db to use for testing
ENV AIRFLOW_CONN_AIRFLOW_METADATA_DB=postgresql+psycopg2://postgres:postgres@postgres:5432/postgres
