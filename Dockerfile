# Dockerfile for building the inference application and Celery Worker
FROM continuumio/miniconda3:latest
COPY ./assets /assets
COPY app.py .
COPY tasks.py .
COPY requirements.txt .
RUN pip3 install -r requirements.txt
RUN apt-get update && apt-get install -y supervisor
COPY confs/supervisord.conf supervisord.conf
EXPOSE 8080
CMD [ "supervisord" ]