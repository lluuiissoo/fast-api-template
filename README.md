# servicemanager-api-customers
API to manage customers

Created with FASTAPI
https://fastapi.tiangolo.com/

## Run locally for dev
uvicorn app.main:app --reload

## Run for PROD
uvicorn app.main:app

## Build docker image
docker build -t servicemanager-api-customers .

## Run docker
docker run -d --name api-customers -p 80:80 servicemanager-api-customers


