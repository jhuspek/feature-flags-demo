# Unleash - Feature Flags Demo Application

This project demonstrates the use of feature flags in a web application, specifically using REST API call. Below you'll
find
detailed instructions on how to set up and use the application.

## Project structure

The project is structured as follows:

- `main.py`: The entry point of the application.
- `config.py`: Configuration settings for the application.
- `routers/`
    - `root.py`: Root route handlers.
    - `api.py`: General API routes.
    - `products.py`: Handles routes related to products.
- `featureflags/`
    - `manager.py`: Handles feature flag operations.
- `domain/`: Contains domain-specific logic and models.

## Prerequisites

Ensure you have `Docker` and `Docker Compose` installed on your machine.

## Building the docker image

To build the Docker image for the demo application, run the following command:

```
docker build -t feature-flags-demo .
```

## Running the application

There is already prepared `docker-compose` with all dependant services.
To start the application using `Docker Compose` run:

```
docker compose up -d
```

This command will start all the necessary services in detached mode.

## Accessing the Unleash dashboard

The demo uses Unleash to manage feature flags. You can access the Unleash dashboard at:

- **URL**: http://localhost:4242
- **Username**: admin
- **Password**: unleash4all

You can explore the OpenAPI reference documentation at http://localhost:4242/docs/openapi.

## Accessing the Feature-Flag-Demo application

Once the application is up and running, you can access the API documentation and interact with the endpoints:

- **API Documentation**: http://localhost:8080/docs
- **Products API**: http://localhost:8080/api/v1/products