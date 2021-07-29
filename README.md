# Run Backend with Docker

## Start App
1. Download and run Docker Desktop: https://www.docker.com/products/docker-desktop
2. To start the backend, run `docker-compose up -d --build`
3. To get the database up and running, run `docker-compose exec backend python manage.py migrate`

### Create Super User
1. The database currently starts from scratch each time, so you will need to create
a super user. Run `docker-compose exec backend python manage.py createsuperuser`

## Shut Down
1. To shut down the instances of Docker, run `docker-compose down`
