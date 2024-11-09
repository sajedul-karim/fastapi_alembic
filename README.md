```markdown:README.md
# FastAPI Project

A robust FastAPI application with MySQL integration, Docker support, and comprehensive development tooling.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
  - [Using Pyenv and Virtualenv](#using-pyenv-and-virtualenv)
  - [Using Docker](#using-docker)
- [Running the Application](#running-the-application)
  - [Local Development](#local-development)
  - [With Docker Compose](#with-docker-compose)
- [API Documentation](#api-documentation)
- [Available API Endpoints](#available-api-endpoints)
- [Development Tools](#development-tools)
  - [Code Formatting with Black](#code-formatting-with-black)
  - [Linting with Ruff](#linting-with-ruff)
  - [Type Checking with MyPy](#type-checking-with-mypy)
  - [Pre-Commit Hooks](#pre-commit-hooks)
- [Docker Configuration](#docker-configuration)
  - [Docker Network](#docker-network)
  - [Docker Compose Services](#docker-compose-services)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Features

- **FastAPI** for building high-performance APIs.
- **MySQL** as the relational database.
- **SQLAlchemy** ORM for database interactions.
- **Docker** and **Docker Compose** for containerization.
- **Development Tools**: Black, Ruff, MyPy, Pre-Commit.

## Prerequisites

- [Python 3.11.5](https://www.python.org/downloads/)
- [Pyenv](https://github.com/pyenv/pyenv)
- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Installation

### Using Pyenv and Virtualenv

1. **Create a Virtual Environment:**

   ```bash
   pyenv virtualenv 3.11.5 fast-3.11.5
   pyenv activate fast-3.11.5
   ```

2. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt
   ```

### Using Docker

1. **Create Docker Network:**

   ```bash
   docker network create fastapi-network
   ```

2. **Set Up MySQL Container:**

   ```bash
   docker run --name fastapi-mysql-db \
     --network fastapi-network \
     -e MYSQL_ROOT_PASSWORD=admin \
     -e MYSQL_DATABASE=fastapi_db \
     -p 3309:3306 \
     -d mysql:8.0
   ```

## Running the Application

### Local Development

1. **Activate Virtual Environment:**

   ```bash
   pyenv activate fast-3.11.5
   ```

2. **Install Python Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application:**

   ```bash
   uvicorn main:app --reload
   ```

4. **Access Swagger UI:**

   Open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) in your browser.

### With Docker Compose

1. **Build and Start Containers:**

   ```bash
   docker-compose up --build
   ```

2. **Access the Application:**

   - **API:** [http://localhost:8000](http://localhost:8000)
   - **Swagger UI:** [http://localhost:8000/docs](http://localhost:8000/docs)

## API Documentation

The API is documented using Swagger UI, which provides an interactive interface to explore and test the available endpoints.

- **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Available API Endpoints

### User Endpoints

- **Create a New User**

  ```http
  POST /user
  ```

  **Request Body:**

  ```json
  {
    "name": "John Doe",
    "email": "john.doe@example.com",
    "password": "securepassword"
  }
  ```

  **Response:**

  ```json
  {
    "id": 1,
    "name": "John Doe",
    "email": "john.doe@example.com"
  }
  ```

- **Retrieve All Users**

  ```http
  GET /users
  ```

  **Response:**

  ```json
  [
    {
      "id": 1,
      "name": "John Doe",
      "email": "john.doe@example.com"
    },
    {
      "id": 2,
      "name": "Jane Smith",
      "email": "jane.smith@example.com"
    }
  ]
  ```

- **Retrieve a Specific User**

  ```http
  GET /user/{user_id}
  ```

  **Response:**

  ```json
  {
    "id": 1,
    "name": "John Doe",
    "email": "john.doe@example.com"
  }
  ```

- **Delete a User**

  ```http
  DELETE /user/{user_id}
  ```

  **Response:**

  ```json
  {
    "message": "User deleted successfully"
  }
  ```

### Post Endpoints

- **Create a New Post**

  ```http
  POST /post
  ```

  **Request Body:**

  ```json
  {
    "title": "My First Post",
    "content": "This is the content of my first post.",
    "published": true,
    "user_id": 1
  }
  ```

  **Response:**

  ```json
  {
    "id": 1,
    "title": "My First Post",
    "content": "This is the content of my first post.",
    "published": true,
    "created_at": "2023-10-05T12:34:56.789Z",
    "user_id": 1
  }
  ```

- **Retrieve All Posts**

  ```http
  GET /posts
  ```

  **Response:**

  ```json
  [
    {
      "id": 1,
      "title": "My First Post",
      "content": "This is the content of my first post.",
      "published": true,
      "created_at": "2023-10-05T12:34:56.789Z",
      "user_id": 1
    },
    {
      "id": 2,
      "title": "Another Post",
      "content": "More content here.",
      "published": false,
      "created_at": "2023-10-06T08:21:45.123Z",
      "user_id": 2
    }
  ]
  ```

- **Retrieve a Specific Post**

  ```http
  GET /post/{post_id}
  ```

  **Response:**

  ```json
  {
    "id": 1,
    "title": "My First Post",
    "content": "This is the content of my first post.",
    "published": true,
    "created_at": "2023-10-05T12:34:56.789Z",
    "user_id": 1
  }
  ```

## Development Tools

### Code Formatting with Black

Ensure code consistency by formatting your code with Black.

```bash
pip install black==24.10.0
black .
```

### Linting with Ruff

Maintain code quality by running Ruff linter.

```bash
pip install ruff==0.7.0
ruff check .
```

### Type Checking with MyPy

Ensure type safety with MyPy.

```bash
pip install mypy==1.12.0
mypy .
```

### Pre-Commit Hooks

Automate code checks before committing.

1. **Install Pre-Commit:**

   ```bash
   pip install pre-commit
   ```

2. **Install Git Hooks:**

   ```bash
   pre-commit install
   ```

3. **Run Pre-Commit Manually (Optional):**

   ```bash
   pre-commit run --all-files
   ```

## Docker Configuration

### Docker Network

A custom Docker network ensures that the `web` and `db` services can communicate.

```bash
docker network create fastapi-network
```

### Docker Compose Services

Define and manage multi-container Docker applications with Docker Compose.

**`docker-compose.yml`**

```yaml:docker-compose.yml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=mysql+pymysql://root:admin@db:3306/fastapi_db
    depends_on:
      db:
        condition: service_healthy
    volumes:
      - .:/app
    networks:
      - app-network

  db:
    image: mysql:8.0
    ports:
      - "3309:3306"
    environment:
      - MYSQL_ROOT_PASSWORD=${MYSQL_ROOT_PASSWORD}
      - MYSQL_DATABASE=${MYSQL_DATABASE}
    volumes:
      - mysql_data:/var/lib/mysql
    networks:
      - app-network
    healthcheck:
      test: ["CMD", "mysqladmin", "ping", "-h", "localhost", "-u", "root", "-padmin"]
      interval: 5s
      timeout: 5s
      retries: 5
      start_period: 30s

volumes:
  mysql_data:

networks:
  app-network:
    driver: bridge
```

**Running with Docker Compose:**

1. **Start Services:**

   ```bash
   docker-compose up --build
   ```

2. **Stop Services:**

   ```bash
   docker-compose down
   ```

3. **Remove All Volumes:**

   ```bash
   docker-compose down -v
   ```

## Project Structure

```
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
├── .gitignore
├── README.md
├── main.py
├── database.py
├── models.py
├── schemas.py
├── services.py
├── requirements.txt
├── requirements-dev.txt
├── wait-for-it.sh
├── pyproject.toml
└── mypy.ini
```

- **Dockerfile:** Defines the Docker image for the FastAPI application.
- **docker-compose.yml:** Configures Docker services.
- **.dockerignore:** Specifies files to ignore in Docker builds.
- **.gitignore:** Specifies files to ignore in version control.
- **README.md:** Project documentation.
- **main.py:** Entry point of the FastAPI application.
- **database.py:** Database configuration and session management.
- **models.py:** SQLAlchemy ORM models.
- **schemas.py:** Pydantic models for request and response validation.
- **services.py:** Business logic and database operations.
- **requirements.txt:** Python dependencies.
- **requirements-dev.txt:** Development-specific dependencies.
- **wait-for-it.sh:** Script to wait for MySQL to be ready before starting the application.
- **pyproject.toml:** Configuration for Black and Ruff.
- **mypy.ini:** Configuration for MyPy.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bugs.

## License

This project is licensed under the [MIT License](LICENSE).
```
