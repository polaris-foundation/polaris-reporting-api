from typing import Optional

from flask import Blueprint, Response, jsonify, make_response

from dhos_reporting_api.blueprint_api import controller

api_blueprint = Blueprint("api_blueprint", __name__)


@api_blueprint.route("/dhos/v1/weekly_active_patients", methods=["PUT"])
def update_weekly_active_patients(
    product_name: str, trust: str, weekly_active_patient_counts: list
) -> Response:
    """
    ---
    put:
      summary: Update the weekly active patient data
      tags: [patient]
      parameters:
        - name: product_name
          in: query
          required: true
          description: Product with which patients should be associated
          schema:
            type: string
            example: GDM
        - name: trust
          in: query
          required: True
          description: Trust code / short name
          schema:
            type: string
            example: DEV
      requestBody:
        x-body-name: weekly_active_patient_counts
        description: List of year-weeks with count of active patients
        required: true
        content:
          application/json:
            schema:
              type: array
              items: WeeklyActivePatientCountsRequest
      responses:
        '204':
          description: Update successful
        default:
          description: >-
            Error, e.g. 400 Bad Request, 503 Service Unavailable
          content:
            application/json:
              schema: Error
    """
    controller.update_weekly_active_patients(
        product_name=product_name,
        trust=trust,
        weekly_active_patient_counts=weekly_active_patient_counts,
    )
    return make_response("", 204)


@api_blueprint.route("/dhos/v1/weekly_active_patients", methods=["GET"])
def get_weekly_active_patients(
    product_name: Optional[str] = None, trust: Optional[str] = None
) -> Response:
    """
    ---
    get:
      summary: Get weekly active patients
      tags: [patient]
      parameters:
        - name: product_name
          in: query
          required: false
          description: Name of product
          schema:
            type: string
            example: GDM
        - name: trust
          in: query
          required: false
          description: Restrict return data to specific Trust
          schema:
            type: string
            example: DEV
      responses:
        '200':
          description: List of active patients by year and week
          content:
            application/json:
              schema:
                type: array
                items: WeeklyActivePatientCountsResponse
        default:
          description: >-
            Error, e.g. 400 Bad Request, 503 Service Unavailable
          content:
            application/json:
              schema: Error
    """

    response: list = controller.get_weekly_active_patients(
        product_name=product_name, trust=trust
    )
    return jsonify(response)


@api_blueprint.route("/dhos/v1/daily_created_patients", methods=["PUT"])
def update_daily_created_patients(
    product_name: str, trust: str, daily_created_patients: list
) -> Response:
    """
    ---
    put:
      summary: Create daily patient count data
      tags: [patient]
      parameters:
        - name: product_name
          in: query
          required: true
          description: Product with which patients should be associated
          schema:
            type: string
            example: GDM
        - name: trust
          in: query
          required: True
          description: Trust code / short name
          schema:
            type: string
            example: DEV
      requestBody:
        x-body-name: daily_created_patients
        description: List of dates with count of created patients
        required: true
        content:
          application/json:
            schema:
              type: array
              items: DailyCreatedPatientCountsRequest
      responses:
        '204':
          description: Update successful
        default:
          description: >-
            Error, e.g. 400 Bad Request, 503 Service Unavailable
          content:
            application/json:
              schema: Error
    """
    controller.update_daily_created_patients(
        product_name=product_name,
        trust=trust,
        daily_created_patients=daily_created_patients,
    )
    return make_response("", 204)


@api_blueprint.route("/dhos/v1/daily_created_patients", methods=["GET"])
def get_daily_created_patients(
    product_name: Optional[str] = None, trust: Optional[str] = None
) -> Response:
    """
    ---
    get:
      summary: Get daily created patients
      tags: [patient]
      parameters:
        - name: product_name
          in: query
          required: false
          description: Name of product
          schema:
            type: string
            example: GDM
        - name: trust
          in: query
          required: false
          description: Restrict return data to specific Trust
          schema:
            type: string
            example: DEV
      responses:
        '200':
          description: List of created patients by date
          content:
            application/json:
              schema:
                type: array
                items: DailyCreatedPatientCountsResponse
        default:
          description: >-
            Error, e.g. 400 Bad Request, 503 Service Unavailable
          content:
            application/json:
              schema: Error
    """

    response: list = controller.get_daily_created_patients(
        product_name=product_name, trust=trust
    )
    return jsonify(response)
