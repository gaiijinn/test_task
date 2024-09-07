Event Management System

Project Description

The Event Management System is an application for creating, managing, and participating in events. Users can create events, add guests, subscribe to events as guests, and unsubscribe from them. The project supports user authentication and email notifications.

Installation and Setup

1) Cloning the repository
git clone https://github.com/gaiijinn/test_task
2) Build the Docker image:
docker-compose build
3) Make database migrations
docker-compose run --rm test_task sh -c "python manage.py makemigrations"
4) Aplly database migrations
docker-compose run --rm test_task sh -c "python manage.py migrate"
5) Start the container
docker-compose up

To view the documentation follow the link:
http://127.0.0.1:8000/api/docs/
Or
http://localhost:8000/api/docs/
