# Architecture Overview

## Components

- **Agent**: Orchestrates planning, execution, and communication.
- **Memory**: Handles persistent storage in MongoDB.
- **Planner**: Decides and executes plans for incoming tasks.
- **Communicator**: Handles agent-to-agent or agent-to-user communication.
- **API**: Exposes endpoints for user and agent interaction.

## Data Flow

1. User submits task via API.
2. Agent receives task, plans action, and executes.
3. Results and task history are saved in MongoDB.
4. User can query past tasks.

## Extending

- Add LLM integration in `planner.py` for advanced reasoning.
- Implement more complex schemas in `tasks.py`.
- Expand `communicator.py` for multi-agent workflows.