#!/bin/bash

SERVER_PORT=${1-5000}
export SERVER_PORT=${SERVER_PORT}
export DATABASE_HOST=localhost
export DATABASE_PORT=5432
export DATABASE_USER=dhos-reporting-api
export DATABASE_PASSWORD=dhos-reporting-api
export DATABASE_NAME=dhos-reporting-api
export ENVIRONMENT=DEVELOPMENT
export ALLOW_DROP_DATA=true
export FLASK_APP=dhos_reporting_api/autoapp.py
export REDIS_INSTALLED=False
export LOG_FORMAT=colour

if [ -z "$*" ]
then
   flask db upgrade
   python -m dhos_reporting_api
else
flask $*
fi
