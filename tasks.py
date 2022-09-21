from celery import Celery
import time
from loguru import logger

app = Celery('ROFL', broker="amqp://rabbitmq:5672",
             backend="mongodb://mongodb:27017/task_results")


# This is the task that celery tries to execute. bind=True specifies the task is
# bound and are required for task retires and accessing the task status


@app.task(bind=True)
def start_processing(self):
    # Lets simulate a long running task here. By long running we are
    # talking even tasks that take just a minute even. Lets pretend to
    # read a file that takes 1 minute to be read, and it contains just
    # a "Hello World"
    logger.info('Reading a book :|')
    with open('assets/temp.txt', 'r') as file:
        result = file.read()
    time.sleep(60)
    logger.info('Done reading a book :)')
    logger.info()
    return result
