# FastAPI Todo Application

A fully-featured REST API for managing todo items with user authentication, built with FastAPI.

## Features

- User registration and authentication with JWT
- Todo items management (CRUD operations)
- Owner-based access control
- Database integration with PostgreSQL and SQLAlchemy
- Docker support for development and production
- Automated testing with pytest
- CI/CD pipeline with GitHub Actions
- Database migrations with Alembic

## Tech Stack

- FastAPI - Web framework
- SQLAlchemy - ORM
- PostgreSQL - Database
- Alembic - Database migrations
- JWT - Authentication
- Pydantic - Data validation
- Docker - Containerization
- GitHub Actions - CI/CD

## Setup Instructions

### 1. Install Python

Make sure you have Python 3.8 or higher installed.  
You can download Python from the [official website](https://www.python.org/downloads/).

To check if Python is already installed, run:
```sh
python --version
```

### 2. Install Pipenv

Pipenv is used for managing dependencies and virtual environments.

To install Pipenv, run:
```sh
pip install pipenv
```

To verify Pipenv installation:
```sh
pipenv --version
```

### 3. Install Project Dependencies

Once Pipenv is installed, run the following command in the project directory to install all dependencies:
```sh
pipenv install
```

For development, install test dependencies:
```sh
pipenv install --dev
```

### 4. Activate Virtual Environment

```sh
pipenv shell
```

## Environment Variables

Create a `.env` file in the root directory with the following variables:

```
DATABASE_HOSTNAME=localhost
DATABASE_PORT=5432
DATABASE_PASSWORD=your_password
DATABASE_NAME=fastapi
DATABASE_USERNAME=postgres
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

## Database Setup

1. Create a PostgreSQL database:
```sh
createdb fastapi
```

2. Run Alembic migrations:
```sh
alembic upgrade head
```

## Running the Application

### Development

```sh
uvicorn app.main:app --reload
```

### Using Docker

Development:
```sh
docker-compose -f docker-compose-dev.yml up -d
```

Production:
```sh
docker-compose -f docker-compose-prod.yml up -d
```

## Deployment

### Azure VM Deployment

This project is configured for deployment to Azure Virtual Machines using GitHub Actions.

The deployment process includes:
1. Automated testing
2. Building Docker images
3. Pushing images to container registry
4. Deploying to Azure VM

For more information about the CI/CD pipeline, see the [CI_CD_README.md](CI_CD_README.md) file.

## API Documentation

Once the application is running, you can access:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Running Tests

```sh
pytest
```

Or, for more detailed output:
```sh
pytest -v
```

## API Endpoints

### Authentication
- `POST /login` - Authenticate user and get token

### Users
- `POST /users` - Create a new user
- `GET /users/{id}` - Get user by ID

### Todo Items
- `GET /todos` - List all todos
- `POST /todos` - Create a new todo
- `GET /todos/{id}` - Get todo by ID
- `PUT /todos/{id}` - Update todo
- `DELETE /todos/{id}` - Delete todo
