MIGRATION_ID = "001_create_indexes"
MIGRATION_NAME = "Create indexes for CRM collections"


def up(db):
    db.users.create_index("email", unique=True, name="idx_users_email_unique")

    db.sailors.create_index(
        [("user_id", 1), ("status", 1)],
        name="idx_sailors_user_status"
    )
    db.sailors.create_index(
        [("user_id", 1), ("created_at", -1)],
        name="idx_sailors_user_created_at"
    )
    db.sailors.create_index(
        [("user_id", 1), ("position", 1)],
        name="idx_sailors_user_position"
    )

    db.companies.create_index(
        [("user_id", 1), ("name", 1)],
        name="idx_companies_user_name"
    )

    db.vacancies.create_index(
        [("user_id", 1), ("status", 1)],
        name="idx_vacancies_user_status"
    )
    db.vacancies.create_index(
        [("user_id", 1), ("start_date", 1)],
        name="idx_vacancies_user_start_date"
    )

    db.contracts.create_index(
        [("user_id", 1), ("status", 1)],
        name="idx_contracts_user_status"
    )
    db.contracts.create_index(
        [("user_id", 1), ("end_date", 1)],
        name="idx_contracts_user_end_date"
    )

    db.pipeline.create_index(
        [("user_id", 1), ("stage", 1)],
        name="idx_pipeline_user_stage"
    )
    db.pipeline.create_index(
        [("user_id", 1), ("vacancy_id", 1)],
        name="idx_pipeline_user_vacancy"
    )