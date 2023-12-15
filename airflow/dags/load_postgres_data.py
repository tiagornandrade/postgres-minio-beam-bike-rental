from airflow import DAG
from airflow.operators.python import PythonOperator
from postgres.utils.generate import GenerateData

default_args = {
    'owner': 'data-engineering',
}

with DAG (
    dag_id='load_postgres_data',
    schedule_interval='0 0 * * *',
    default_args=default_args,
    catchup=False,
    on_failure_callback=failed_slack_notification
) as dag:

    create_stations = PythonOperator(
        python_callable=GenerateData.create_stations,
        op_args="None",
        op_kwargs="None",
        templates_dict="None",
        templates_exts="None",
        show_return_value_in_logs="True",
    )
