# Run Backend with Docker

## Start App
1. Download and run Docker Desktop: https://www.docker.com/products/docker-desktop
2. To start the backend, run `docker-compose up -d --build`
3. To get the database up and running, run `docker-compose exec backend python manage.py migrate`

## Shut Down
1. To shut down the instances of Docker, run `docker-compose down`
