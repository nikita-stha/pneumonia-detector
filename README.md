# Pnuemonia Detector
A simple web application to detect pnuemonia.

## Demo
You can try this project [here in replit](https://replit.com/@nikita-stha/CancerDetection?v=1).

[Screencast from 03-18-2023 01:37:06 PM.webm](https://user-images.githubusercontent.com/66687885/226152452-c3a40ce2-3cd4-41eb-91d4-cba3da860fd4.webm)


## System Requirements
- Python3
- Twilio Account (https://www.twilio.com/try-twilio)
- Twilio ACCOUNT_SID & AUTH_TOKEN
- Huggingface Inference API token. (Your model needs to be deployed in huggingface)
- [Link to Colab Notebook for the model used.](https://colab.research.google.com/drive/1wdhTEFm4_As7XMzXDjflHhxK3MUWSjRn?usp=sharing)
- [Link to model deployed in huggingface] (https://huggingface.co/niki-stha/vit-pneumonia-detector)
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
