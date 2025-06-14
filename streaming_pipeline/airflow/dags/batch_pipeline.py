from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    "owner": "serhii",
    "retries": 1,
    "retry_delay": timedelta(minutes=2)
}

with DAG(
    dag_id="batch_pipeline_dag",
    default_args=default_args,
    description="ETL pipeline: landing → bronze → silver → gold",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False,
    tags=["final", "goit"]
) as dag:

    landing_to_bronze = BashOperator(
        task_id="landing_to_bronze",
        bash_command="/home/serhii/spark/bin/spark-submit /mnt/d/Projects/repositories/goit-de-fp/streaming_pipeline/batch_pipeline/landing_to_bronze.py"
    )

    bronze_to_silver = BashOperator(
        task_id="bronze_to_silver",
        bash_command="/home/serhii/spark/bin/spark-submit /mnt/d/Projects/repositories/goit-de-fp/streaming_pipeline/batch_pipeline/bronze_to_silver.py"
    )

    silver_to_gold = BashOperator(
        task_id="silver_to_gold",
        bash_command="/home/serhii/spark/bin/spark-submit /mnt/d/Projects/repositories/goit-de-fp/streaming_pipeline/batch_pipeline/silver_to_gold.py"
    )

    landing_to_bronze >> bronze_to_silver >> silver_to_gold
