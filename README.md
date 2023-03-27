# Pnuemonia Detector
A simple web application to detect pnuemonia.

## System Requirements
- Python3
- Twilio Account (https://www.twilio.com/try-twilio)
- Twilio ACCOUNT_SID & AUTH_TOKEN
- Huggingface Inference API token. (Your model needs to be deployed in huggingface)
- Docker for local ( development & deployent)
- Docker-compose
- In file web/project/constants.py Update the phone number that you will use for Text message alert.

## Quickstart Guide for Local Development

1. First clone this repository through 

`https://github.com/nikita-stha/pneumonia-detector.git`

2. Run`cd pneumonia-detector`

3. Run `cp .env.example .env.dev`

4. Run `chmod 755 services/web/entrypoint.sh` to resolve permission issues.

5. Run `docker-compose up -d --build`

You can access web application on: http://localhost:5000/

## Quickstart Guide for Local Deployment

1. Run `cp .env.example .env.prod`

2. Run `chmod 755 services/web/entrypoint.prod.sh` to resolve permission issues.

3. Run `docker-compose -f docker-compose.prod.yml up -d --build`

You can access web application on: http://localhost:1337/
