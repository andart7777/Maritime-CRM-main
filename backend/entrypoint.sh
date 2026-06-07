#!/bin/sh

set -e

echo "Waiting for MongoDB..."

python - <<'PY'
import os
import time
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError

mongo_url = os.environ.get("MONGO_URL", "mongodb://mongo:27017")

for attempt in range(30):
    try:
        client = MongoClient(mongo_url, serverSelectionTimeoutMS=1000)
        client.admin.command("ping")
        print("MongoDB is ready")
        break
    except ServerSelectionTimeoutError:
        print(f"MongoDB is not ready yet. Attempt {attempt + 1}/30")
        time.sleep(1)
else:
    raise RuntimeError("MongoDB connection failed")
PY

echo "Running migrations..."
python migrations/run_migrations.py

echo "Starting backend..."
python server.py
