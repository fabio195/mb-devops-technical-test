import logging
import os

import requests
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Query

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
def get_people(page: int = Query(1, ge=1)):
    try:
        logger.info(f"Fetching people data from SWAPI, page {page}")

        if not SWAPI_URL:
            logger.error("SWAPI_URL is not set")
            raise HTTPException(
                status_code=500, detail="Internal server error: SWAPI_URL is not set"
            )

        # Make a request to the SWAPI with the specified page number
        response = requests.get(f"{SWAPI_URL}/people", params={"page": page})
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)

        people_data = response.json()

        # Extract and sort people by "name" attribute
        people_list = people_data["results"]
        people_sorted_by_name = sorted(people_list, key=lambda person: person["name"])

        logger.info(f"Successfully fetched and sorted people data from page {page}")
        return {"people_sorted_by_name": people_sorted_by_name}

    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching data from SWAPI: {e}")
        raise HTTPException(
            status_code=502, detail="Bad Gateway: Error fetching data from SWAPI"
        )

    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
