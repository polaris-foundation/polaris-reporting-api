# -*- coding: utf-8 -*-

from flask_batteries_included.sqldb import db
from she_logging.logging import logger


def reset_database() -> None:
    """Drops SQL data"""
    try:
        for model in ["ActivePatients"]:
            db.session.query(model).delete()
        db.session.commit()
    except Exception:
        logger.exception("Drop SQL data failed")
        db.session.rollback()
