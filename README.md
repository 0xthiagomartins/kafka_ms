# Microservice Template with Kafka Integration

## Introduction

This template provides a basic structure for a microservice using Nameko with Kafka integration. It includes essential configurations and sample code to get you started with a Kafka-enabled microservice.

## Folder Structure

- `src/service.py`: The main service class that handles microservice logic and dependencies such as logs and database connections.
- `src/business/`: Folder for business logic of the microservice.
- `src/config.yml`: Configuration file for broker settings.
- `run.py`: Script to run the microservice.
- `run.sh`: Script to run tests and call `run.py`.
- `docker-compose.yml`: Docker Compose configuration for setting up Kafka, Zookeeper, and the microservice.
- `Dockerfile`: Docker configuration for building the microservice image.
- `tests/`: Folder for unit tests using pytest.
- `README.md`: Documentation for the project.

## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Running the Microservice

1. Build and start the services using Docker Compose:

   ```bash
   docker-compose up --build
