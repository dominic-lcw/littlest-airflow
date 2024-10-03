#!/bin/bash

# Airflow requires a home directory. Default to be the ${root}/airflow.
export AIRFLOW_HOME="$(pwd)"/airflow

# Initialize the Airflow database
airflow db migrate

# Create an Airflow user
airflow users create \
    --username airflow \
    --password airflow \
    --firstname Peter \
    --lastname Parker \
    --role Admin \
    --email spiderman@superhero.org

# # Start the Airflow webserver
# airflow webserver --port 8080 &

# # # Start the Airflow scheduler
# airflow scheduler &