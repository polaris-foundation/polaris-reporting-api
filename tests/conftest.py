import json
from typing import Callable, Dict, Generator, List, Type, Union

import pytest
from flask import Flask
from flask_batteries_included.sqldb import db
from marshmallow import RAISE, Schema


@pytest.fixture(scope="session")
def session_app() -> Flask:
    import dhos_reporting_api.app

    return dhos_reporting_api.app.create_app(testing=True)


@pytest.fixture
def app() -> Flask:
    """ "Fixture that creates app for testing"""
    from dhos_reporting_api.app import create_app

    current_app = create_app(testing=True, use_pgsql=False, use_sqlite=True)
    return current_app


@pytest.fixture
def app_context(app: Flask) -> Generator[None, None, None]:
    with app.app_context():
        yield


@pytest.fixture
def assert_valid_schema(
    app: Flask,
) -> Callable[[Type[Schema], Union[Dict, List], bool], None]:
    def verify_schema(
        schema: Type[Schema], value: Union[Dict, List], many: bool = False
    ) -> None:
        # Roundtrip through JSON to convert datetime values to strings.
        serialised = json.loads(json.dumps(value, cls=app.json_encoder))
        schema().load(serialised, many=many, unknown=RAISE)

    return verify_schema


@pytest.fixture
def clear_sql_database() -> None:
    db.session.commit()
    db.drop_all()
    db.create_all()
