from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="athlete_events_batch_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False
) as dag:

    run_spark_job = BashOperator(
        task_id="run_spark_etl",
        bash_command="spark-submit /opt/airflow/dags/../spark_job.py"
    )
