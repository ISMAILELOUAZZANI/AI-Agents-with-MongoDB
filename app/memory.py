from datetime import datetime

class Memory:
    def __init__(self, agent_id, db):
        self.agent_id = agent_id
        self.db = db

    def save_task(self, task, output):
        doc = {
            "agent_id": self.agent_id,
            "created_at": datetime.utcnow().isoformat(),
            "task": task,
            "output": output
        }
        self.db.tasks.insert_one(doc)

    def get_tasks(self):
        return list(self.db.tasks.find({"agent_id": self.agent_id}))