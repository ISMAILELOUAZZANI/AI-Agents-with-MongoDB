from app.memory import Memory
from app.planner import Planner
from app.communicator import Communicator

class Agent:
    def __init__(self, agent_id, db):
        self.agent_id = agent_id
        self.memory = Memory(agent_id, db)
        self.planner = Planner(self.memory)
        self.communicator = Communicator()

    def handle_task(self, task):
        plan = self.planner.plan(task)
        result = self.planner.execute(plan)
        self.memory.save_task(task, result)
        return result