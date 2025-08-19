# CI/CD Setup for FastAPI Project

This repository uses GitHub Actions for Continuous Integration and Continuous Deployment.

## CI/CD Pipeline

The CI/CD pipeline consists of three main stages:

1. **Test**: Runs the test suite against a PostgreSQL database
2. **Build and Push**: Builds a Docker image and pushes it to DockerHub
3. **Deploy**: Deploys the application to a server using Docker Compose

## GitHub Secrets Required

To use this CI/CD pipeline, you need to add the following secrets to your GitHub repository:

- `DOCKERHUB_USERNAME`: Your DockerHub username
- `DOCKERHUB_TOKEN`: Your DockerHub access token
- `SERVER_HOST`: The hostname or IP address of your deployment server
- `SERVER_USERNAME`: The username to SSH into your deployment server
- `SERVER_SSH_KEY`: The SSH private key to access your deployment server

## Running Tests Locally

To run tests locally:

```bash
# Set environment variables
export DATABASE_HOSTNAME=localhost
export DATABASE_PORT=5432
export DATABASE_PASSWORD=password
export DATABASE_NAME=fastapi_test
export DATABASE_USERNAME=postgres
export SECRET_KEY=testsecretkey
export ALGORITHM=HS256
export ACCESS_TOKEN_EXPIRE_MINUTES=30

# Run tests
pytest
```

## Deployment Process

The deployment process:

1. The GitHub Actions workflow builds and pushes a Docker image to DockerHub
2. The workflow then SSHs into the deployment server
3. It pulls the latest Docker image and restarts the containers

To modify the deployment path, edit the `deploy` job in the `.github/workflows/ci-cd.yml` file.
