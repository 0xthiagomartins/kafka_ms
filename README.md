# Microservice Template with Kafka Integration

## Introduction

This template provides a basic structure for a microservice using Nameko with Kafka integration. It includes essential configurations and sample code to get you started with a Kafka-enabled microservice.

## Folder Structure

- `src/service.py`: The main service class that handles microservice logic and dependencies such as logs and database connections.
- `src/business/`: Folder for business logic of the microservice.
- `src/config.yml`: Configuration file for broker settings.
- `src/config.py`: Python module to load configurations.
- `run.py`: Script to run the microservice.
- `run.sh`: Script to run tests and call `run.py`.
- `docker-compose.yml`: Docker Compose configuration for setting up the microservice.
- `Dockerfile`: Docker configuration for building the microservice image.
- `tests/`: Folder for unit tests using pytest.
- `README.md`: Documentation for the project.

## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Running the Microservice

1. Build and start the microservice using Docker Compose:

   ```bash
   docker-compose up --build
   ```

2. The microservice will connect to the Kafka and Zookeeper instances on the configured network.

### Configuration

src/config.yml contains the default configuration for Kafka bootstrap servers, service name, and topic name.
Environment variables can override these defaults when running the service.

### Example Usage

The MicroServiceA class in src/service.py demonstrates how to produce and consume messages using Kafka within a Nameko service.

### Testing

Run tests using the provided script:

    ```bash
    ./run.sh
    ```

### Conclusion 

This template provides a starting point for developing Kafka-integrated microservices with Nameko. Modify the provided code and configurations to suit your specific requirements.

This setup centralizes configuration using config.yml and environment variables, ensuring consistency across different environments. Adjust the configurations and scripts as needed.