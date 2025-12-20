Airport API Service
Airport API Service is a Django + PostgreSQL web service for managing airports, flights, and bookings via a REST API. Fully containerized with Docker, it includes automated tests, database readiness checks (wait_for_db), and dependency management via requirements.txt.

Tech Stack: Python 3.13, Django, DRF, PostgreSQL, Docker, Pytest, Flake8

Run:

docker-compose up -d --build
docker-compose exec app python manage.py migrate
docker-compose exec app python manage.py test

Test Users: testuser, testuser01

API available at http://localhost:8000/
