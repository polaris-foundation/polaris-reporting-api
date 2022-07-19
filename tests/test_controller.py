import pytest

from dhos_reporting_api.blueprint_api.controller import (
    get_daily_created_patients,
    get_weekly_active_patients,
    update_daily_created_patients,
    update_weekly_active_patients,
)


@pytest.mark.usefixtures("app", "clear_sql_database")
class TestController:
    def test_update_get_weekly_active_patients(self) -> None:
        update: list = [
            {"year_week": "2022-1", "count": 5},
            {"year_week": "2022-2", "count": 10},
        ]
        expected: list = [
            {"year_week": "2022-1", "count": 5, "trust": "DEV", "product_name": "GDM"},
            {"year_week": "2022-2", "count": 10, "trust": "DEV", "product_name": "GDM"},
        ]

        update_weekly_active_patients(
            product_name="GDM", trust="DEV", weekly_active_patient_counts=update
        )
        assert get_weekly_active_patients(product_name="GDM", trust="DEV") == expected

    def test_conflicting_weekly_update(self) -> None:
        update_1: list = [
            {"year_week": "2022-1", "count": 5},
            {"year_week": "2022-2", "count": 10},
        ]
        update_2: list = [
            {"year_week": "2022-2", "count": 15},
            {"year_week": "2022-3", "count": 20},
        ]
        expected: list = [
            {"year_week": "2022-1", "count": 5, "trust": "DEV", "product_name": "GDM"},
            {"year_week": "2022-2", "count": 15, "trust": "DEV", "product_name": "GDM"},
            {"year_week": "2022-3", "count": 20, "trust": "DEV", "product_name": "GDM"},
        ]

        update_weekly_active_patients(
            product_name="GDM", trust="DEV", weekly_active_patient_counts=update_1
        )
        update_weekly_active_patients(
            product_name="GDM", trust="DEV", weekly_active_patient_counts=update_2
        )
        assert get_weekly_active_patients(product_name="GDM", trust="DEV") == expected

    def test_update_daily_created_patients(self) -> None:
        update: list = [
            {"date": "2022-01-01", "count": 5},
            {"date": "2022-01-02", "count": 10},
        ]
        expected: list = [
            {"date": "2022-01-01", "count": 5, "trust": "DEV", "product_name": "GDM"},
            {"date": "2022-01-02", "count": 10, "trust": "DEV", "product_name": "GDM"},
        ]

        update_daily_created_patients(
            product_name="GDM", trust="DEV", daily_created_patients=update
        )
        assert get_daily_created_patients(product_name="GDM", trust="DEV") == expected

    def test_conflicting_daily_update(self) -> None:
        update_1: list = [
            {"date": "2022-01-01", "count": 5},
            {"date": "2022-01-02", "count": 10},
        ]
        update_2: list = [
            {"date": "2022-01-02", "count": 20},
            {"date": "2022-01-03", "count": 10},
        ]
        expected: list = [
            {
                "date": "2022-01-01",
                "count": 5,
                "trust": "DEV",
                "product_name": "GDM",
            },
            {
                "date": "2022-01-02",
                "count": 20,
                "trust": "DEV",
                "product_name": "GDM",
            },
            {
                "date": "2022-01-03",
                "count": 10,
                "trust": "DEV",
                "product_name": "GDM",
            },
        ]

        update_daily_created_patients(
            product_name="GDM", trust="DEV", daily_created_patients=update_1
        )
        update_daily_created_patients(
            product_name="GDM", trust="DEV", daily_created_patients=update_2
        )
        assert get_daily_created_patients(product_name="GDM", trust="DEV") == expected
