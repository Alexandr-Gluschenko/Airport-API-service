Airport API Service

Airport API Service is a RESTful web application built with Django and Django REST Framework for managing airport-related data such as airports, flights, and bookings.
The service is fully containerized with Docker and uses PostgreSQL as the primary database. It follows modern backend development practices, including automated testing, code quality checks, and environment isolation.

The project is designed as a backend service and exposes a JSON-based REST API that can be consumed by frontend applications or third-party services.

Features :

- CRUD operations for airports, flights, and bookings

- REST API built with Django REST Framework

- PostgreSQL as the main database

- Docker & Docker Compose for containerized development

- Database readiness handling (wait_for_db)

- Automated tests using Pytest

- Code style and linting with Flake8

- Environment-independent setup

Tech Stack:

- Python 3.13
- Django
- Django REST Framework
- PostgreSQL
- Docker & Docker Compose
- Pytest
- Flake8

Running the Project Make sure Docker and Docker Compose are installed.

docker-compose up -d --build
docker-compose exec app python manage.py migrate
docker-compose exec app python manage.py test


API Access After startup, the API is available at:
http://localhost:8000/

Test Users 
Username: testuser 
Password: testuser01
