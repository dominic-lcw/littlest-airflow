# Airflow Playground

## Setup
- Python Virtual Environments
- Kubectl
- Docker
- Image Registry
- Kubernetes Cluster on AWS or GCP

## Extra Components
- Database

## Folders
- Dag folders
- Log folders

## Executors
- Local Executor
- Celery Executor
- Kubernetes Executor

# Run Airflow Locally
```bash
# Run the services
docker run -d -p 8080:8080 airflow webserver
docker run -d -p 8080:8080 airflow scheduler
```
-d is to run in daemon mode




