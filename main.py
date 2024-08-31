import os

import requests
from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()

# Environment variables
SWAPI_URL = os.getenv("SWAPI_URL")

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Welcome to the SWAPI API!"}


@app.get("/people")
def get_people():
    response = requests.get(SWAPI_URL + "/people")
    people_data = response.json()

    # Sort people by "name" attribute
    people_sorted_by_name = sorted(
        people_data["results"], key=lambda person: person["name"]
    )
    return {"people_sorted_by_name": people_sorted_by_name}
