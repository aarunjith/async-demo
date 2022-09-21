# Lets create a simple FastAPI service which listens to our API calls
# to start processing our task

from fastapi import FastAPI
from celery.result import AsyncResult
from tasks import start_processing
from loguru import logger
from pymongo import MongoClient
import uvicorn

# Lets create a connection to our backend where celery stores the results
client = MongoClient("mongodb://mongodb:27017")

# Default database and collection names that Celery create
db = client['task_results']
coll = db["celery_taskmeta"]

app = FastAPI()


@app.post('/process')
async def process_text_file():
    '''
    Process endpoint to trigger the start of a process
    '''
    try:
        result = start_processing.delay()
        logger.info(f'Started processing the task with id {result.id}')
        return {
            "status": result.state,
            'id': result.id,
            'error': ''
        }
    except Exception as e:
        logger.info(f'Task Execution failed: {e}')
        return {
            "status": "FAILURE",
            'id': None,
            'error': e
        }


@app.post('/check_progress/{task_id}')
async def check_async_progress(task_id: str):
    '''
    Endpoint to check the task progress and fetch the results if the task is
    complete.
    '''
    try:
        result = AsyncResult(task_id)
        if result.ready():
            data = coll.find({'_id': task_id})[0]
            return {'status': 'SUCEESS', 'data': data['result']}
        else:
            return {"status": result.state, "error": ''}
    except Exception as e:
        data = coll.find({'_id': task_id})[0]
        if data:
            return {'status': 'SUCEESS', 'data': data['result']}
        return {'status': 'Task ID invalid', 'error': e}

if __name__ == "__main__":
    uvicorn.run("app:app", host='0.0.0.0', port='8080')
