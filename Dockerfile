# Use Ubuntu as base image
FROM ubuntu:latest

# Install Python and pip
RUN apt-get update && apt-get install -y python3-3.11.9 python3-pip

# Upgrade pip
RUN pip install --upgrade pip

# Install Airflow
RUN pip install apache-airflow==2.9.3 'apache-airflow[kubernetes]'

# Set working directory
WORKDIR /home

# Set Entry point
COPY bootstrap.sh /bootstrap.sh
RUN chmod +x /bootstrap.sh
ENTRYPOINT ["/bootstrap.sh"]