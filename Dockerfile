FROM python:3.12.7-bookworm

# Specify workdir and user
WORKDIR /home

# Copy requirements.txt and install dependencies
COPY ../requirements.txt .
RUN pip install -r requirements.txt

# Customized airflow setup
ENV AIRFLOW_HOME=/home/littlest-airflow \
  PYTHONPATH=/home/littlest-airflow
COPY . .
