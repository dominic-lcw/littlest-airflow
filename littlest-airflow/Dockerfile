FROM python:3.12.11-trixie

USER root

RUN pip install uv

ENV AIRFLOW_VERSION=3.0.4
ENV PYTHON_VERSION=3.12
ENV CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"

# Install apache-airflow with --system flag
RUN uv pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}" --system

# Create airflow directories
RUN mkdir -p /opt/airflow/dags /opt/airflow/plugins /opt/airflow/logs /opt/airflow/config

# Copy and install requirements
COPY requirements.txt /
RUN pip install --no-cache-dir -r /requirements.txt

# Copy application files
COPY src/dags /opt/airflow/dags
COPY src/plugins /opt/airflow/plugins
COPY src/config/airflow.cfg /opt/airflow/airflow.cfg

# Set AIRFLOW_HOME environment variable
ENV AIRFLOW_HOME=/opt/airflow

# Environment variables for admin user
ENV AIRFLOW_ADMIN_USERNAME=admin
ENV AIRFLOW_ADMIN_PASSWORD=littlest123
ENV AIRFLOW_ADMIN_EMAIL=admin@littlest-airflow.com
ENV AIRFLOW_ADMIN_FIRSTNAME=Littlest
ENV AIRFLOW_ADMIN_LASTNAME=Admin

# JWT secret for API authentication
ENV AIRFLOW__API_AUTH__JWT_SECRET=your-secret-key-here-change-in-production

# Copy initialization script
COPY init-airflow.sh /init-airflow.sh
RUN chmod +x /init-airflow.sh

EXPOSE 8080

CMD ["/init-airflow.sh"]