from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from opendota.config import entities
from opendota.scripts.manager import fetch_data_from_opendota

with DAG(
    dag_id="opendota_dag",
    schedule_interval="@daily",
    start_date=datetime(2026, 4, 1),
    catchup=True,
    max_active_runs=1,
) as dag:
    python_operator = PythonOperator(
        task_id="python_operator",
        python_callable=fetch_data_from_opendota,
        op_kwargs={
            "entities": entities,
        },
    )

    python_operator