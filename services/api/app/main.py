import os
from pathlib import Path
from fastapi import FastAPI
from dotenv import load_dotenv
from pymongo import MongoClient

ENV_PATH = Path(__file__).resolve().parents[1] / ".env"
load_dotenv(dotenv_path=ENV_PATH)

app = FastAPI(title="CS Capstone API", version="0.1.0")

def mongo_ok() -> bool:
    uri = os.getenv("MONGO_URI")
    if not uri:
        return False
    client = MongoClient(uri, serverSelectionTimeoutMS=2000)
    client.admin.command("ping")
    return True

@app.get("/health")
def health():
    mongo_status = "down"
    try:
        mongo_status = "ok" if mongo_ok() else "missing_env"
    except Exception:
        mongo_status = "down"

    return {"status": "ok", "mongo": mongo_status}