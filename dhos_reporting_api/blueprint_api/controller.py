from datetime import date
from typing import Optional

from flask_batteries_included.sqldb import db
from sqlalchemy.dialects.postgresql import insert

from dhos_reporting_api.models.active_patients import ActivePatients
from dhos_reporting_api.models.created_patients import CreatedPatients


def update_weekly_active_patients(
    product_name: str, trust: str, weekly_active_patient_counts: list
) -> None:
    active_patients: list[dict] = [
        w | {"product_name": product_name, "trust": trust}
        for w in weekly_active_patient_counts
    ]

    stmt = insert(ActivePatients).values(active_patients)
    table = ActivePatients.__table__
    stmt = stmt.on_conflict_do_update(
        constraint=table.primary_key, set_={"count": stmt.excluded.count}
    )
    db.session.execute(stmt)
    db.session.commit()


def get_weekly_active_patients(
    product_name: Optional[str], trust: Optional[str]
) -> list:
    query = db.session.query(ActivePatients)
    if product_name:
        query.filter(ActivePatients.product_name == product_name)
    if trust:
        query.filter(ActivePatients.trust == trust)
    return [ap.to_dict() for ap in query.all()]


def update_daily_created_patients(
    product_name: str, trust: str, daily_created_patients: list
) -> None:
    created_patients: list[dict] = [
        {
            "product_name": product_name,
            "trust": trust,
            "date": date.fromisoformat(daily_count["date"]),
            "count": daily_count["count"],
        }
        for daily_count in daily_created_patients
    ]

    stmt = insert(CreatedPatients).values(created_patients)
    table = CreatedPatients.__table__
    stmt = stmt.on_conflict_do_update(
        constraint=table.primary_key, set_={"count": stmt.excluded.count}
    )
    db.session.execute(stmt)
    db.session.commit()


def get_daily_created_patients(
    product_name: Optional[str], trust: Optional[str]
) -> list:
    query = db.session.query(CreatedPatients)
    if product_name:
        query.filter(CreatedPatients.product_name == product_name)
    if trust:
        query.filter(CreatedPatients.trust == trust)
    return [cp.to_dict() for cp in query]
