from typing import Dict

from flask import Flask
from flask.ctx import AppContext
from flask.testing import FlaskClient


class TestDevRoutes:
    def test_drop_data_prod(
        self,
        app: Flask,
        client: FlaskClient,
        app_context: AppContext,
        jwt_system: Dict,
    ) -> None:
        app.config["ENVIRONMENT"] = "PRODUCTION"
        response = client.post("/drop_data")
        assert response.status_code == 403

    def test_drop_data_non_prod(
        self,
        app: Flask,
        client: FlaskClient,
        app_context: AppContext,
        jwt_system: Dict,
    ) -> None:
        app.config["ALLOW_DROP_DATA"] = True
        app.config["ENVIRONMENT"] = "TRAINING"
        response = client.post("/drop_data")
        assert response.status_code == 200
