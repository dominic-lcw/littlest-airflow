CREATE DATABASE airflow_db;
CREATE USER airflow_user WITH PASSWORD 'airflow_pass';

-- Grant usage on the public schema
GRANT USAGE ON SCHEMA public TO airflow_user;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO airflow_user;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO airflow_user;
GRANT ALL PRIVILEGES ON ALL FUNCTIONS IN SCHEMA public TO airflow_user;