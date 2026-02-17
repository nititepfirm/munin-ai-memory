from fastapi import FastAPI
import chromadb
from chromadb.config import Settings
import os

app = FastAPI(title="Munin API", description="AI Memory Service", version="0.1.0")

# Initialize ChromaDB
DB_PATH = os.getenv("CHROMA_DB_PATH", "./munin_brain")
client = chromadb.PersistentClient(path=DB_PATH)
collection = client.get_or_create_collection(name="memories")

@app.get("/")
def health_check():
    return {"status": "ok", "service": "Munin"}

@app.get("/stats")
def get_stats():
    return {
        "count": collection.count(),
        "db_path": DB_PATH
    }
