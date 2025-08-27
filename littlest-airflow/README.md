# littlest-airflow Project

## Overview
This project is a minimal setup for deploying Apache Airflow using a single container. It includes an example Directed Acyclic Graph (DAG), configuration files, and necessary dependencies to get started with Airflow.

## Project Structure
```
littlest-airflow
├── src
│   ├── dags
│   │   └── example_dag.py
│   ├── plugins
│   └── config
│       └── airflow.cfg
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## Getting Started

### Prerequisites
- Docker
- Docker Compose

### Setup Instructions
1. Clone the repository:
   ```
   git clone <repository-url>
   cd littlest-airflow
   ```

2. Build the Docker image:
   ```
   docker-compose build
   ```

3. Start the Airflow services:
   ```
   docker-compose up
   ```

### Accessing Airflow
Once the services are up and running, you can access the Airflow web interface at `http://localhost:8080`. The default username and password are both set to `airflow`.

### Example DAG
The example DAG can be found in `src/dags/example_dag.py`. This file contains a simple workflow that demonstrates how to define tasks and their dependencies using the Airflow API.

### Custom Plugins
You can add custom plugins in the `src/plugins` directory. This allows you to extend Airflow's functionality by creating custom operators, sensors, or hooks.

### Configuration
The Airflow configuration can be modified in `src/config/airflow.cfg`. This file contains settings for the Airflow environment, including executor type and database connection details.

### Requirements
All Python dependencies are listed in `requirements.txt`. Make sure to review this file to understand the libraries required for your DAGs and plugins.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.