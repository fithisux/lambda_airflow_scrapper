"Contains profile mappings used in the project"

from cosmos import ProfileConfig
from cosmos.profiles import PostgresUserPasswordProfileMapping

airflow_db = ProfileConfig(
    profile_name="imdb_dataset_article",
    target_name="dev",
    profiles_yml_filepath='/usr/local/airflow/dbt/imdb_dataset_article/profiles.yml'
    # profile_mapping=PostgresUserPasswordProfileMapping(
    #     conn_id="aws_aa_db",
    #     profile_args={'schema': 'dbt'}
    # ),
)
