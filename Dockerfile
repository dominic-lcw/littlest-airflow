FROM python:3.12 

# Add your instructions here
RUN pip install --upgrade pip \
    && pip install apache-airflow==2.9.3 \ 
    && pip install 'apache-airflow[kubernetes]'

WORKDIR /home

# Set Entry point
COPY bootstrap.sh /bootstrap.sh
RUN chmod +x /bootstrap.sh
ENTRYPOINT ["/bootstrap.sh"]