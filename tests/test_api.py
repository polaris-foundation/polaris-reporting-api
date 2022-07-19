import pytest
from flask.testing import FlaskClient
from mock import Mock
from pytest_mock import MockerFixture

from dhos_reporting_api.blueprint_api import controller


@pytest.mark.usefixtures("app")
class TestApi:
    def test_update_weekly_active_patients(
        self, mocker: MockerFixture, client: FlaskClient
    ) -> None:
        weekly_update: list = [
            {"year_week": "2022-1", "count": 10},
            {"year_week": "2022-2", "count": 20},
        ]
        mock_create: Mock = mocker.patch.object(
            controller,
            "update_weekly_active_patients",
            return_value=None,
        )
        response = client.put(
            "/dhos/v1/weekly_active_patients?product_name=GDM&trust=DEV",
            json=weekly_update,
            headers={"Authorization": "Bearer TOKEN"},
        )
        assert response.status_code == 204
        mock_create.assert_called_with(
            product_name="GDM", trust="DEV", weekly_active_patient_counts=weekly_update
        )

    def test_get_weekly_active_patients(
        self, mocker: MockerFixture, client: FlaskClient
    ) -> None:
        weekly_data: list = [
            {"year_week": "2022-1", "count": 10, "product_name": "GDM", "trust": "DEV"},
            {"year_week": "2022-2", "count": 20, "product_name": "GDM", "trust": "DEV"},
        ]
        mock_get: Mock = mocker.patch.object(
            controller,
            "get_weekly_active_patients",
            return_value=weekly_data,
        )
        response = client.get(
            "/dhos/v1/weekly_active_patients?product_name=GDM&trust=DEV",
            headers={"Authorization": "Bearer TOKEN"},
        )
        assert response.status_code == 200
        mock_get.assert_called_with(product_name="GDM", trust="DEV")

    @pytest.mark.usefixtures("clear_sql_database")
    def test_full_update_weekly_active_patients(
        self,
        client: FlaskClient,
    ) -> None:
        weekly_update: list = [
            {"year_week": "2022-1", "count": 10},
            {"year_week": "2022-2", "count": 20},
        ]
        expected: list = [
            {"year_week": "2022-1", "count": 10, "product_name": "GDM", "trust": "DEV"},
            {"year_week": "2022-2", "count": 20, "product_name": "GDM", "trust": "DEV"},
        ]
        client.put(
            "/dhos/v1/weekly_active_patients?product_name=GDM&trust=DEV",
            json=weekly_update,
            headers={"Authorization": "Bearer TOKEN"},
        )
        response = client.get(
            "/dhos/v1/weekly_active_patients?product_name=GDM&trust=DEV",
            headers={"Authorization": "Bearer TOKEN"},
        )
        assert response.status_code == 200
        assert response.json == expected

    def test_fully_update_daily_created_patients(
        self, mocker: MockerFixture, client: FlaskClient
    ) -> None:
        daily_update: list = [
            {"date": "2022-01-01", "count": 10},
            {"date": "2022-01-02", "count": 20},
        ]
        expected: list = [
            {"date": "2022-01-01", "count": 10, "product_name": "GDM", "trust": "DEV"},
            {"date": "2022-01-02", "count": 20, "product_name": "GDM", "trust": "DEV"},
        ]
        response = client.put(
            "/dhos/v1/daily_created_patients?product_name=GDM&trust=DEV",
            json=daily_update,
            headers={"Authorization": "Bearer TOKEN"},
        )
        assert response.status_code == 204
        response = client.get(
            "/dhos/v1/daily_created_patients?product_name=GDM&trust=DEV",
            headers={"Authorization": "Bearer TOKEN"},
        )
        assert response.status_code == 200
        assert response.json == expected
