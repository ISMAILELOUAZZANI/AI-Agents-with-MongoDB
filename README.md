# AI Agents with MongoDB

A modular framework for building autonomous AI agents with persistent memory and knowledge using MongoDB.

## Features

- Modular, extensible AI agent architecture
- Persistent memory and task history via MongoDB
- Pluggable planners, communicators, and memory modules
- REST API for interaction (FastAPI)
- Example agents and sample tasks

## Quick Start

1. Clone the repo  
2. Install requirements: `pip install -r requirements.txt`  
3. Set MongoDB connection string in `.env`
4. Run the API:  
   ```
   uvicorn api.main:app --reload
   ```
5. Explore `/docs` for API usage

## Project Structure

See `docs/architecture.md` for more details.