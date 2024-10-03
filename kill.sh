#!/bin/bash

echo $(AIRFLOW_HOME)
kill $(cat $AIRFLOW_HOME/airflow-scheduler.pid)
kill $(cat $AIRFLOW_HOME/airflow-webserver.pid)