import os
import requests

API_URL = "https://api-inference.huggingface.co/models/niki-stha/vit-pneumonia-detector"


def query(filename):
    headers = {"Authorization": os.getenv("HUGGINGFACE_INFERENCE_API_TOKEN")}
    try:
        with open(filename, "rb") as f:
            data = f.read()
        response = requests.post(API_URL, headers=headers, data=data)
        response = response.json()
        return (
            response[0] if response[0]["score"] > response[1]["score"] else response[1]
        )
    except:
        return response
