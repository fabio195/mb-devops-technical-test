# MB DevOps Technical Test

This repository holds the files and configurations to resolve a DevOps Technical Test.

## Table of Contents
 - [Test Description](#test-description)
	  - [Objective](#objective)
	  - [Technical Requirements](#technical-requirements)
	  - [Containerization and Orchestration](#containerization-and-orchestration)
	  - [Evaluation](#evaluation)
 - [Documentation of resolution](#documentation-of-resolution)
	 - [Prerequisites](#prerequisites)
	 - [Environment Variables](#environment-variables)
	 - [Usage](#usage)
	 - [Preparation](#preparation)
	 - [Docker Compose execution](#docker-compose-execution)
	 - [Kubernetes execution](#kubernetes-execution)
	 - [API Endpoints](#api-endpoints)
	 - [Error Handling](#error-handling)
	 - [Logging](#logging)
 - [Resources Used](#resources-used)

# Test description
## Objective
Implement and deploy a microservice that interacts with the SWAPI - The Star Wars API demonstrating proficiency in software development, containerization, orchestration, and performance optimization.

## Technical Requirements

 - Implement the microservice in one of the following languages: Golang, Java, or Python.
 - The microservice should consume the people endpoint from the Star Wars API.
 - Fetch the data from the people endpoint.
 - Sort the fetched data in ascending order based on the name attribute.
 - Create an endpoint in your microservice that returns the sorted data.
 - Include error handling and logging.

## Containerization and Orchestration

 - Containerize the microservice using Docker.
 - Write a Docker Compose file to run the service and dependencies locally.
 - Deploy the service to a local Kubernetes cluster (minikube or kind).

## Evaluation

 - **Code Quality:** Clarity, maintainability, and adherence to language-specific conventions.
 - **Functionality:** Fulfillment of the acceptance criteria and proper functioning of the microservice.
 - **Deployment:** Successful deployment using Docker, Docker Compose, and Kubernetes.
 - **Documentation:** Clear instructions, explanations, and comments.

# Documentation of resolution
## Prerequisites
- [Docker](https://docs.docker.com/get-started/get-docker/) installed.
- [Docker Compose](https://docs.docker.com/compose/) installed.
- [Minikube](https://minikube.sigs.k8s.io/docs/) installed.
- [Kubectl](https://kubernetes.io/docs/reference/kubectl/) installed.

## Environment Variables
The application relies on an environment variable to connect to the SWAPI.

```text
SWAPI_URL="https://swapi.dev/api/"
```
## Usage
The resolution comes in two ways of usage:
1. Docker Compose.
2. Kubernetes.

## Preparation

1. Clone the repository:
   ```bash
   git clone https://github.com/fabio195/mb-devops-technical-test
   cd mb-devops-technical-test
   ```

### Docker Compose execution

1. Run the following command in order to Build and Deploy a Docker container using Docker Compose:
   ```bash
   docker compose up --build
   ```
   This code will search the file called `docker-compose.yaml` and interpret it in order to build and deploy the service.
   You will be able to use the service by navigating in your browser to `localhost:8000`

### Kubernetes execution
1. Make sure you have Minikube started:
	```bash
	minikube start
	minikube status
	```
2. Navigate into the `kubernetes_config` directory:
	```bash
	cd kubernetes_config
	```
3. Modify the `deployment.yaml` file to match the latest version of the image available on the [Docker Hub Registry](https://hub.docker.com/repository/docker/fabio195/swapi-api/tags)
4. Deploy the `deployment.yaml` file, which contains the definition of the Deployment object, using the following command:
	```bash
	kubectl apply -f deployment.yaml
	```
5. Deploy the `service.yaml` file, which contains the definition of the Service object, configured as NodePort, in order to enable communication between the Minikube Node and the local machine, to enable traffic through a local port, in this case, port 30000:
	```bash
	kubectl apply -f service.yaml
	```
6. Check that everything is working properly:
	```bash
	kubectl get pods
	kubectl get services
	```
7. To access the service, we need the internal IP provided by Kubernetes to access the Service. To get this, run the following command:
	```bash
	minikube service swapi-api --url
	```
	This command will print an IP followed by the port defined in the service. For example: http://192.168.49.2:30000 (The IP may change in your local environment)
	You will be able to use the service by navigating in your browser to the provided IP + Port



## API Endpoints
Available endpoints, including descriptions, parameters, and example requests and responses.

### GET `/`
- **Description:** Returns a welcome message.
- **Response:**
  ```json
  {
    "message": "Welcome to the SWAPI API!"
  }
  ```

### GET `/people`
- **Description:** Fetches and returns a list of Star Wars characters sorted by name.
- **Parameters:**
  - `page`: (Optional) The page number to retrieve (default is 1).
- **Example Request:**
  ```bash
  curl -X GET "http://127.0.0.1:8000/people?page=1"
  ```
- **Example Response:**
  ```json
  {
  "people_sorted_by_name": [
    {
      "name": "Beru Whitesun lars",
      "height": "165",
      "mass": "75",
      "hair_color": "brown",
      "skin_color": "light",
      "eye_color": "blue",
      "birth_year": "47BBY",
      "gender": "female",
      "homeworld": "https://swapi.dev/api/planets/1/",
      "films": [
        "https://swapi.dev/api/films/1/",
        "https://swapi.dev/api/films/5/",
        "https://swapi.dev/api/films/6/"
      ],
      "species": [],
      "vehicles": [],
      "starships": [],
      "created": "2014-12-10T15:53:41.121000Z",
      "edited": "2014-12-20T21:17:50.319000Z",
      "url": "https://swapi.dev/api/people/7/"
    },
    {
      "name": "Biggs Darklighter",
      "height": "183",
      "mass": "84",
      "hair_color": "black",
      "skin_color": "light",
      "eye_color": "brown",
      "birth_year": "24BBY",
      "gender": "male",
      "homeworld": "https://swapi.dev/api/planets/1/",
      "films": [
        "https://swapi.dev/api/films/1/"
      ],
      "species": [],
      "vehicles": [],
      "starships": [
        "https://swapi.dev/api/starships/12/"
      ],
      "created": "2014-12-10T15:59:50.509000Z",
      "edited": "2014-12-20T21:17:50.323000Z",
      "url": "https://swapi.dev/api/people/9/"
    },
    ...
  ]
  }
  ```

## Error Handling

The API handles errors gracefully and returns appropriate HTTP status codes along with error messages.

- **500 Internal Server Error:** If the SWAPI URL is not set or an unexpected error occurs.
  ```json
  {
    "detail": "Internal server error: SWAPI_URL is not set"
  }
  ```

- **502 Bad Gateway:** If there's an issue fetching data from SWAPI.
  ```json
  {
    "detail": "Bad Gateway: Error fetching data from SWAPI"
  }
  ```

## Logging

The application uses Python's built-in logging module to log information and errors. Logs are written to the console by default, providing insights into API requests and internal processing.

# Resources Used
For solving this test, the following resources were used:

- [Fast API](https://fastapi.tiangolo.com/): Web framework for building APIs with Python based on standard Python type hints.
- [Docker](https://docs.docker.com/get-started/get-docker/): Used to build container images.
- [Docker Compose](https://docs.docker.com/compose/): Used to deploy the container images and use the service running on a container.
- [Minikube](https://minikube.sigs.k8s.io/docs/): Used to deploy the service on a local kubernetes-like environment.
- [Kubectl](https://kubernetes.io/docs/reference/kubectl/): Used to communicate with Minikube in order to deploy the service.
- [SonarLint](#https://www.sonarsource.com/products/sonarlint/): Used to get real time feedback about the code being writed.
- [Pre Commit](#https://pre-commit.com/): Used to identifying simple issues before submission to code review. In addition with Pre Commit Hooks to fix these issues and enforce best practices.

#### GitHub Workflow
Every time you push into this repository, a GitHub Action is triggered.
In this Action, the Docker image is built automatically and pushed to Docker Hub Registry.
