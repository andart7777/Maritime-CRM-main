import importlib.util
import os
from datetime import datetime, timezone
from pathlib import Path

from dotenv import load_dotenv
from pymongo import MongoClient


MIGRATIONS_DIR = Path(__file__).resolve().parent


def load_migration_module(path: Path):
    spec = importlib.util.spec_from_file_location(path.stem, path)
    module = importlib.util.module_from_spec(spec)

    if spec.loader is None:
        raise RuntimeError(f"Cannot load migration file: {path}")

    spec.loader.exec_module(module)
    return module


def get_migration_files():
    return sorted(
        path
        for path in MIGRATIONS_DIR.glob("m*.py")
        if path.name != "__init__.py"
    )


def run_migrations(db):
    db.schema_migrations.create_index("migration_id", unique=True)

    applied_migrations = {
        item["migration_id"]
        for item in db.schema_migrations.find({}, {"migration_id": 1})
    }

    for path in get_migration_files():
        module = load_migration_module(path)

        migration_id = getattr(module, "MIGRATION_ID", None)
        migration_name = getattr(module, "MIGRATION_NAME", path.stem)

        if not migration_id:
            raise RuntimeError(f"Migration {path.name} does not contain MIGRATION_ID")

        if migration_id in applied_migrations:
            print(f"Skipped migration: {migration_id}")
            continue

        print(f"Applying migration: {migration_id} - {migration_name}")
        module.up(db)

        db.schema_migrations.insert_one(
            {
                "migration_id": migration_id,
                "name": migration_name,
                "applied_at": datetime.now(timezone.utc),
            }
        )

        print(f"Applied migration: {migration_id}")


def main():
    backend_dir = MIGRATIONS_DIR.parent
    load_dotenv(backend_dir / ".env")

    mongo_url = os.environ.get("MONGO_URL", "mongodb://localhost:27017")
    db_name = os.environ.get("DB_NAME", "Maritime-CRM")

    client = MongoClient(mongo_url)
    db = client[db_name]
    print(f"Using MongoDB database: {db_name}")

    run_migrations(db)


if __name__ == "__main__":
    main()