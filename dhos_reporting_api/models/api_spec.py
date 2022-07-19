from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin
from flask_batteries_included.helpers.apispec import (
    FlaskBatteriesPlugin,
    Identifier,
    initialise_apispec,
    openapi_schema,
)
from marshmallow import EXCLUDE, Schema, fields

dhos_reporting_api_spec: APISpec = APISpec(
    version="1.0.0",
    openapi_version="3.0.3",
    title="DHOS Reporting API",
    info={"description": "A service for reporting PMCF information"},
    plugins=[FlaskPlugin(), MarshmallowPlugin(), FlaskBatteriesPlugin()],
)

initialise_apispec(dhos_reporting_api_spec)


class WeeklyActivePatientCountsRequest(Schema):
    class Meta:
        unknown = EXCLUDE
        ordered = True

    year_week = fields.String(
        required=True,
        metadata={
            "description": "The year and week that the data covers",
            "example": "2021-33",
        },
    )
    count = fields.Integer(
        required=True,
        metadata={
            "description": "Total count of active patients in time period",
            "example": 100,
        },
    )


class WeeklyActivePatientCountsResponse(WeeklyActivePatientCountsRequest):
    class Meta:
        unknown = EXCLUDE
        ordered = True

    product_name = fields.String(
        required=True,
        metadata={
            "description": "The name of the product for which the patients are active",
            "example": "GDM",
        },
    )

    trust = fields.String(
        required=True,
        metadata={
            "description": "Name of the Trust where these patients are active",
            "example": "DEV",
        },
    )


class DailyCreatedPatientCountsRequest(Schema):
    class Meta:
        unknown = EXCLUDE
        ordered = True

    date = fields.Date(
        required=True,
        metadata={
            "description": "The day the data covers",
            "example": "2021-01-01",
        },
    )
    count = fields.Integer(
        required=True,
        metadata={
            "description": "Total count of active patients in time period",
            "example": 100,
        },
    )


class DailyCreatedPatientCountsResponse(DailyCreatedPatientCountsRequest):
    class Meta:
        unknown = EXCLUDE
        ordered = True

    product_name = fields.String(
        required=True,
        metadata={
            "description": "The name of the product for which the patients are created",
            "example": "GDM",
        },
    )

    trust = fields.String(
        required=True,
        metadata={
            "description": "Name of the Trust where these patients are created",
            "example": "DEV",
        },
    )
