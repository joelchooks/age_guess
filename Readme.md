# README.md

## Age Guess APP

Description of the project.

### How to Run the Project

1. Clone the repository.
2. Navigate to the project directory.

### Development
3. For Localhost, Run `docker-compose up --build` to start and build the application.
4. Access the API at `http://localhost:8001/api/human-age/`.
5. To access the bash, Run `docker exec -it age_guess_web bash`
6. To view the logs, Run `docker logs -f`
7. To run tests, Run `docker-compose -f run web /opt/venv/bin/python manage.py test`

### Production
3. For Production, Run `docker compose -f docker-compose.prod.yml up -d --build` to start and build the application.
4. Access the API at `http://{{domain}}/api/human-age/`.
5. To access the bash, Run `docker exec -t age_guess_web bash`
6. To view the logs, Run `docker logs -f`
7. To run tests, Run `docker-compose -f docker-compose.prod.yml run web /opt/venv/bin/python manage.py test`
