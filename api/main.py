from fastapi import FastAPI, HTTPException
from app.database import get_db
from app.agent import Agent
from app.tasks import validate_task

app = FastAPI()
db = get_db()
agent = Agent("agent_001", db)

@app.post("/task/")
def submit_task(task: str):
    try:
        validate_task(task)
        result = agent.handle_task(task)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/tasks/")
def list_tasks():
    return agent.memory.get_tasks()