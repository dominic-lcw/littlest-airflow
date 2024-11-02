# Airflow

This repository shows airflow using the littlest setup.

# Deploy

```bash
## Build image
docker build -t littlest-airflow:latest .
## Run image
docker-compose up -d
```

Then the webserver can be viewed at [localhost:8080](http://localhost:8080)

# Debug

We can use SQLite to debug airflow.
To mimic the same setup, but with SQLite as the config, we use the below setup

```json
# Settings.json
"terminal.integrated.env.osx": {
  // This tells the airflow where airflow.cfg is.
    "AIRFLOW_HOME": "/Users/dominicleung/Developer/littlest-airflow/littlest-airflow",
  // This overrides [core-executor]
    "AIRFLOW__CORE__EXECUTOR": "SequentialExecutor",
  // This overrides [database-sql_alchemy_conn]
    "AIRFLOW__DATABASE__SQL_ALCHEMY_CONN": "sqlite:////Users/dominicleung/Developer/airflow/airflow.db"
  },
```
