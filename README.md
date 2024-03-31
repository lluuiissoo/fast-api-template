# servicemanager-api-customers
API to manage customers

Created with FASTAPI
https://fastapi.tiangolo.com/

## Local Dev

### Activate venv
.\.venv\Scripts\Activate.ps1

### Restore deps
pip install -r requirements.txt

### Run locally for dev
uvicorn app.main:app --reload

### Run tests
pytest

### Linter
pylint app --errors-only

## Production

### Run for PROD
uvicorn app.main:app

## Build docker image
docker build -t servicemanager-api-customers .

## Run docker
docker run -d --name api-customers -p 5001:5000 servicemanager-api-customers


