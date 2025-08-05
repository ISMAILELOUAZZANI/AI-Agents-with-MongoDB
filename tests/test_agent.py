import unittest
from app.agent import Agent
from app.memory import Memory

class DummyDB:
    def __init__(self):
        self.tasks = []

    def insert_one(self, doc):
        self.tasks.append(doc)

    def find(self, query):
        return self.tasks

class TestAgent(unittest.TestCase):
    def test_handle_task(self):
        db = DummyDB()
        agent = Agent("agent_test", db)
        result = agent.handle_task("Test task")
        self.assertIn("Executed plan", result)
        self.assertEqual(len(agent.memory.get_tasks()), 1)

if __name__ == "__main__":
    unittest.main()