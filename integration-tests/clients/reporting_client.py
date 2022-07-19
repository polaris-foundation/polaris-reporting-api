from typing import List

import requests
from environs import Env
from requests import Response


def _get_base_url() -> str:
    base_url: str = Env().str(
        "DHOS_REPORTING_BASE_URL", "http://dhos-reporting-api:5000"
    )
    return f"{base_url}"


def get_running() -> Response:
    return requests.get(
        f"{_get_base_url()}/running",
        timeout=15,
    )


def upload_weekly_report(data: List[dict], trust: str, product_name: str) -> Response:
    return requests.put(
        f"{_get_base_url()}/dhos/v1/weekly_active_patients?trust={trust}&product_name={product_name}",
        json=data,
        timeout=15,
    )


def get_weekly_report(trust: str, product_name: str) -> Response:
    return requests.get(
        f"{_get_base_url()}/dhos/v1/weekly_active_patients?trust={trust}&product_name={product_name}",
        timeout=15,
    )


def upload_daily_report(data: List[dict], trust: str, product_name: str) -> Response:
    return requests.put(
        f"{_get_base_url()}/dhos/v1/daily_created_patients?trust={trust}&product_name={product_name}",
        json=data,
        timeout=15,
    )


def get_daily_report(trust: str, product_name: str) -> Response:
    return requests.get(
        f"{_get_base_url()}/dhos/v1/daily_created_patients?trust={trust}&product_name={product_name}",
        timeout=15,
    )
