#!/bin/bash

# Exit on any error
set -e

echo "Starting Airflow initialization..."

# Initialize the database
echo 'Initializing Airflow database...'
airflow db migrate

# Create admin user if it doesn't exist
echo 'Creating admin user...'
airflow users create \
    --username "${AIRFLOW_ADMIN_USERNAME:-admin}" \
    --firstname "${AIRFLOW_ADMIN_FIRSTNAME:-Admin}" \
    --lastname "${AIRFLOW_ADMIN_LASTNAME:-User}" \
    --role Admin \
    --email "${AIRFLOW_ADMIN_EMAIL:-admin@example.com}" \
    --password "${AIRFLOW_ADMIN_PASSWORD:-admin}" 2>/dev/null || echo 'User already exists, skipping creation'

echo "Initialization complete. Starting Airflow services..."

# Function to handle shutdown
shutdown() {
    echo "Shutting down Airflow services..."
    kill $SCHEDULER_PID $WEBSERVER_PID 2>/dev/null || true
    wait
    exit 0
}

# Set up signal handlers
trap shutdown SIGTERM SIGINT

# Start the scheduler in the background
echo "Starting Airflow scheduler..."
airflow scheduler &
SCHEDULER_PID=$!

# Start the webserver in the background
echo "Starting Airflow webserver..."
airflow api-server --port 8080 &
WEBSERVER_PID=$!

echo "Airflow services started:"
echo "  Scheduler PID: $SCHEDULER_PID"
echo "  Webserver PID: $WEBSERVER_PID"
echo "  Webserver available at: http://localhost:8080"

# Wait for both processes
wait
