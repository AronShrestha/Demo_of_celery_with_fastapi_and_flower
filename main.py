from fastapi import FastAPI
from fastapi.responses import JSONResponse
from celery_worker import create_task
from celery.result import AsyncResult


app = FastAPI()


@app.get("/")
async def root():
    return {"message":"Setup complete Champ"}


@app.get('/celery/{time_req}')
async def complete_task(time_req: str):
    task = create_task.delay(int(time_req),10,20)
    print("Printing task ",task)
    return JSONResponse({"task_id":task.id})


@app.get('/result/{task_id}')
async def get_result(task_id:str):
    task_res = AsyncResult(task_id)
    result = {
        "task":task_id,
        "task_status":task_res.status,
        "task_result":task_res.result
    }
    return JSONResponse(result)




