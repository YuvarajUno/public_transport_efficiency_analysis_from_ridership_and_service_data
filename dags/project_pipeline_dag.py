from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys
import os

# Project src folder path-ஐ சேர்க்கவும்
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Import project module functions
from data_ingestion.load_data import load_ridership, load_upcoming_cities
from data_cleaning.clean_data import clean_ridership, clean_upcoming_cities
from feature_engineering.features import add_peak_offpeak_flag, calculate_load_factor
from modeling.simple_model import aggregate_ridership_by_peak
from evaluation.generate_outputs import (
    generate_rq1_table,
    plot_rq2_figure,
    plot_rq3_figure,
    generate_rq3_table,
    generate_rq4_table,
)

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 1, 1),
    'retries': 1,
}

with DAG(
    dag_id='project_pipeline_dag',
    default_args=default_args,
    description='Public Transport Efficiency Analysis Pipeline',
    schedule_interval='@daily',
    catchup=False,
    max_active_runs=1,
) as dag:

    def task_load_data():
        global ridership_df, upcoming_cities_df
        ridership_df = load_ridership('../data/Ridership.csv')
        upcoming_cities_df = load_upcoming_cities('../data/upcoming_city.csv')

    def task_clean_data():
        global ridership_df, upcoming_cities_df
        ridership_df = clean_ridership(ridership_df)
        upcoming_cities_df = clean_upcoming_cities(upcoming_cities_df)

    def task_feature_engineering():
        global ridership_df
        ridership_df = add_peak_offpeak_flag(ridership_df)
        ridership_df = calculate_load_factor(ridership_df)

    def task_modeling():
        global ridership_df
        summary = aggregate_ridership_by_peak(ridership_df)
        print("Modeling summary (peak/off-peak ridership):")
        print(summary)

    def task_generate_outputs():
        global ridership_df
        generate_rq1_table(ridership_df)
        plot_rq2_figure(ridership_df)
        plot_rq3_figure(ridership_df)
        generate_rq3_table(ridership_df)
        generate_rq4_table(ridership_df)

    load_data = PythonOperator(
        task_id='load_data',
        python_callable=task_load_data,
    )

    clean_data = PythonOperator(
        task_id='clean_data',
        python_callable=task_clean_data,
    )

    feature_engineering = PythonOperator(
        task_id='feature_engineering',
        python_callable=task_feature_engineering,
    )

    modeling = PythonOperator(
        task_id='modeling',
        python_callable=task_modeling,
    )

    generate_outputs = PythonOperator(
        task_id='generate_outputs',
        python_callable=task_generate_outputs,
    )

    # Task dependency chain (corrected with '>>' instead of '&gt;&gt;')
    load_data >> clean_data >> feature_engineering >> modeling >> generate_outputs
