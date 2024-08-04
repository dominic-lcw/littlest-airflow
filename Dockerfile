# Use Ubuntu as base image
FROM ubuntu:latest

# Set working directory
WORKDIR /home

# Install Python and pip
RUN apt-get update && apt-get install -y python3 python3-pip

# Install Airflow
RUN pip3 install apache-airflow==2.9.3 'apache-airflow[kubernetes]' --break-system-packages

# Set Entry point
COPY bootstrap.sh /bootstrap.sh
RUN chmod +x /bootstrap.sh
ENTRYPOINT ["/bootstrap.sh"]