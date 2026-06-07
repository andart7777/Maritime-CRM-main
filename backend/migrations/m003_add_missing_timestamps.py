from datetime import datetime, timezone


MIGRATION_ID = "003_add_missing_timestamps"
MIGRATION_NAME = "Add missing created_at fields"


def up(db):
    now = datetime.now(timezone.utc)

    collections = [
        "users",
        "sailors",
        "companies",
        "vacancies",
        "contracts",
        "pipeline",
    ]

    for collection_name in collections:
        result = db[collection_name].update_many(
            {"created_at": {"$exists": False}},
            {
                "$set": {
                    "created_at": now,
                }
            },
        )

        print(
            f"{collection_name}: added created_at to {result.modified_count} documents"
        )