from datetime import datetime, timezone


MIGRATION_ID = "002_backfill_user_id"
MIGRATION_NAME = "Backfill missing user_id fields in demo collections"


def up(db):
    admin = db.users.find_one({"role": "admin"})

    if not admin:
        print("Admin user not found. Backfill skipped.")
        return

    admin_id = str(admin["_id"])
    now = datetime.now(timezone.utc)

    collections = [
        "sailors",
        "companies",
        "vacancies",
        "contracts",
        "pipeline",
    ]

    missing_user_id_filter = {
        "$or": [
            {"user_id": {"$exists": False}},
            {"user_id": None},
            {"user_id": ""},
        ]
    }

    for collection_name in collections:
        result = db[collection_name].update_many(
            missing_user_id_filter,
            {
                "$set": {
                    "user_id": admin_id,
                    "updated_at": now,
                }
            },
        )

        print(
            f"{collection_name}: updated {result.modified_count} documents with user_id"
        )