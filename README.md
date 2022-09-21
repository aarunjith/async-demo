# Asyncronous Processing pipelines in Python

<table><tr>
<td><img src="https://ckl-website-static.s3.amazonaws.com/wp-content/uploads/2020/06/celery_512-300x300.png" alt="Celery" width="150"/></td>
<td><img src="https://cdn.iconscout.com/icon/free/png-256/rabbitmq-282296.png" alt="rabbitmq" width="150"/></td>
<td><img src="https://miro.medium.com/max/1023/1*du7p50wS_fIsaC_lR18qsg.png" alt="fastapi" width="150"/></td>
<td><img src="https://logonoid.com/images/mongodb-logo.png" alt="mongodb" width="150"/></td>
<td><img src="https://logos-download.com/wp-content/uploads/2016/09/Docker_logo.png" alt="docker" width="150"/></td>
</tr></table>
Set up an async pipeline in python using Celery, RabbitMQ and MongoDB. This repo covers the end to end deployment of an async pipeline for your projects using Docker

# Quickstart

1. Clone the repo
2. Make sure Docker and Docker Compose are installed
```bash
$ pip install docker-compose
```
3. Start the docker containers
```bash
$ docker compose up --build
```
4. Check the pipeline using FastAPI endpoints
```bash
# To start processing a task
$ curl -X POST http://localhost:8080/process
# To check the progress of a task
$ curl -X POST http://localhost:8080/check_progress/<task_id>
```
# Setting up your tasks
You can use this pipline to run your custom tasks. You just have to modify the [tasks.py](https://github.com/aarunjith/async-demo/blob/main/tasks.py) and connect it to a fastapi endpoint for trigger
