


# Apache Airflow

Note: Apache Airflow is a workflow and sheduling tool that is configured with Python.

I used docker images and docker-compose to set the environment to experiment.
Good tutrial is https://github.com/tuanavu/airflow-tutorial

(/Playground/airflow-tutorial)

The following `docker-compose.yml` runs and starts the docker images for the posgres backed and the airflow webserver.
In order to load and modyfy the workflow files (dags) a local volume is mapped to the 

```
version: '3'
services:
  postgres:
    image: postgres:9.6
    environment:
      - POSTGRES_USER=airflow
      - POSTGRES_PASSWORD=airflow
      - POSTGRES_DB=airflow

  webserver:
    image: puckel/docker-airflow:1.10.3
    restart: always
    depends_on:
      - postgres
    environment:
      - LOAD_EX=n
      - EXECUTOR=Local
      - FERNET_KEY=jsDPRErfv8Z_eVTnGfF8ywd19j4pyqE3NpdUBA_oRTo=
    volumes:
      - /Users/aortner/Playground/airflow-tutorial/examples:/usr/local/airflow
      # Uncomment to include custom plugins
      # - ./plugins:/usr/local/airflow/plugins
    ports:
      - "8099:8080"
    command: webserver
    healthcheck:
      test: ["CMD-SHELL", "[ -f /usr/local/airflow/airflow-webserver.pid ]"]
      interval: 30s
      timeout: 30s
      retries: 3
```

the docker can then be started via
```
docker-compose up -d
# or
docker-compose -f docker-compose.yml up 

# - f allows to give path and file
# - d runs the process in the background and no log is shwown

```

the airflow ui runns on port 8099 and can be accesed via http://localhost:8099/

and stoped via
```
docker-compose down
```