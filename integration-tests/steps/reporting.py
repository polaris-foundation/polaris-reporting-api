from typing import Dict, List

from behave import step
from behave.runner import Context
from clients import reporting_client
from requests import Response


@step("System is running")
def system_running(context: Context) -> None:
    pass


@step("the running endpoint returns as expected")
def get_running_endpoint(context: Context) -> None:
    response: Response = reporting_client.get_running()
    context.response = response
    assert response.status_code == 200


@step("a weekly patient report is uploaded")
def upload_weekly_patient_report(context: Context) -> None:
    data: List[Dict] = [
        {"year_week": "2022-01", "count": 10},
        {"year_week": "2022-02", "count": 20},
    ]
    response: Response = reporting_client.upload_weekly_report(data, "DEV", "GDM")
    context.response = response
    assert response.status_code == 204


@step("the weekly patient report is available")
def get_weekly_patient_report(context: Context) -> None:
    expected: List[Dict] = [
        {"year_week": "2022-01", "count": 10, "product_name": "GDM", "trust": "DEV"},
        {"year_week": "2022-02", "count": 20, "product_name": "GDM", "trust": "DEV"},
    ]
    response: Response = reporting_client.get_weekly_report("DEV", "GDM")
    context.response = response
    assert response.status_code == 200
    assert response.json() == expected


@step("a daily created report is uploaded")
def upload_daily_patient_report(context: Context) -> None:
    data: List[Dict] = [
        {"date": "2022-01-01", "count": 10},
        {"date": "2022-01-02", "count": 20},
    ]
    response: Response = reporting_client.upload_daily_report(data, "DEV", "GDM")
    context.response = response
    assert response.status_code == 204


@step("the daily created report is available")
def get_daily_patient_report(context: Context) -> None:
    expected: List[Dict] = [
        {"date": "2022-01-01", "count": 10, "product_name": "GDM", "trust": "DEV"},
        {"date": "2022-01-02", "count": 20, "product_name": "GDM", "trust": "DEV"},
    ]
    response: Response = reporting_client.get_daily_report("DEV", "GDM")
    context.response = response
    assert response.status_code == 200
    assert response.json() == expected
