import logging
import os

import requests
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException

load_dotenv()

# Environment variables
SWAPI_URL = os.getenv("SWAPI_URL")

app = FastAPI()

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@app.get("/")
def root():
    logger.info("Root endpoint called")
    return {"message": "Welcome to the SWAPI API!"}


@app.get("/people")
def get_people():
    try:
        logger.info("Fetching people data from SWAPI")

        if not SWAPI_URL:
            logger.error("SWAPI_URL is not set")
            raise HTTPException(
                status_code=500, detail="Internal server error: SWAPI_URL is not set"
            )

        response = requests.get(SWAPI_URL + "/people")
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)

        people_data = response.json()

        # Sort people by "name" attribute
        # Extract the list of people that are returned from the query
        people_list = people_data["results"]

        def get_person_name(person):
            return person["name"]

        # Sort the list of people using the function
        people_sorted_by_name = sorted(people_list, key=get_person_name)

        logger.info("Successfully fetched and sorted people data")
        return {"people_sorted_by_name": people_sorted_by_name}

    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching data from SWAPI: {e}")
        raise HTTPException(
            status_code=502, detail="Bad Gateway: Error fetching data from SWAPI"
        )

    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
