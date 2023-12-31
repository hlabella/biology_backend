# Biology Quiz API

## Overview
- **GET /questions:** Return 5 random biology quiz questions from the database:
-- Question Text: The main text of the question.
-- Choices: Multiple-choice options for the question.
-- Focos: Additional focus points or hints.
-- Image: Visual aids, if applicable, to enhance understanding.
-- Video Resolution: Links to explanatory videos, offering in-depth insights or clarifications.
-- Discipline: The specific discipline within biology that the question pertains to.
-- Thematic: The overarching theme or topic of the question.

- **POST /answer:** Allow users to submit question id and answer text to receive feedback about:
-- Correctness of the Submitted Answer: Indicates whether the user’s answer was correct.
-- Correct Answer: Provides the correct answer for learning purposes.
-- Video Resolution: Offers an optional video explanation, allowing users to understand the rationale behind the correct answer, thereby enriching the learning experience.


## Docker Setup

1. Build the container image:

```bash
docker build -t biology-api-app-repository .
```

2. Run the container:

```bash
docker run -p 8000:8000 biology-api-app-repository
```

3. `https://localhost:8000` should be up and running.

## Dockerhub Image:

You can pull my image from: https://hub.docker.com/repository/docker/hlabellacosta/biology-api-app-repository/general

```bash
docker pull hlabellacosta/biology-api-app-repository:latest
```

Then run the container:

```bash
docker run -d --name biology-api-app-repository -p 8000:8000 hlabellacosta/biology-api-app-repository:latest
```

`https://localhost:8000` should be up and running.

### Try it:

On windows powershell, you can try the API: 

GET /questions endpoint: 
```bash
curl http://localhost:8000/biology_api_app/questions/
```

POST /answer endpoint: 
```bash
curl.exe -H "Content-Type: application/json" -d '{\"question_id\": \"6512e2b5fd7b465b02516710\", \"submitted_answer\": \"favorecem a adapta\u00e7\u00e3o de plantas lenhosas madeireiras.\"}' 'http://localhost:8000/biology_api_app/answer/'

```


## Local Setup - if you need to change database or test:

To start development server at http://127.0.0.1:8000/

```bash
python manage.py runserver
```

The api will be available at:

GET /127.0.0.1:8000/biology_api_app/questions

POST /127.0.0.1:8000/biology_api_app/answer

The database can be re-built using:

```bash
python manage.py import_questions ENEM_biologia.questions.json
```

To change the database, just change the .json file and run again. It will delete every entry and recreate from scratch.

### Tests

Tests can be run with

```bash
python manage.py test
```


## Cloud Deployment

### Prerequisites

- Python
- Docker and login to your Docker Account.
- Azure CLI and login to your Azure account.

### Deploying to Azure

Configure deploy.sh

Ensure you have Docker installed on your machine.

Install the Azure CLI and log in to your Azure account using az login.

Create an Azure Container Registry (ACR) and have its name handy.

Have the deploy.sh script in your project's root directory.

Steps to Deploy:

Open Terminal or Command Prompt:
Navigate to your project's root directory where the deploy.sh script is located.

Make the Script Executable (if on Unix/Linux/Mac):
```bash
chmod +x deploy.sh
```
Execute the script by typing:
```bash
./deploy.sh
```

This will start the deployment process.

### Deployment steps:

Define Variables:
The script starts by defining several variables used throughout the deployment process, such as image name, container name, resource group, registry name, and port number.

Build the Docker Image:
The Docker image of your application is built using the docker build command. This image contains all the necessary code and dependencies to run your application.

Authenticate with Azure Container Registry (ACR):
The script logs into your ACR using az acr login. This step is crucial for pushing your Docker image to your private registry in Azure.

Tag the Docker Image:
The Docker image is then tagged with the ACR name. Tagging is essential for organizing and managing different versions of your Docker images in the registry.

Push the Image to Azure Container Registry:
The tagged image is pushed to your Azure Container Registry using docker push. This step uploads your image to Azure, making it available for deployment.

Deploy the Image to Azure Container Instances (ACI):
Finally, the script uses the az container create command to deploy the image to Azure Container Instances. This command specifies the resource group, container name, image to use (from ACR), DNS name label, ports, and IP address settings. It creates a container instance that runs your application and makes it accessible over the internet.

### Accessing the Application

Once deployed, you will have the URL and you can use the endpoints

# Check it out:

GET endpoint: http://biology-api-app.cuggbpbhetg7fncv.brazilsouth.azurecontainer.io:8000/biology_api_app/questions/

```bash
curl http://biology-api-app.cuggbpbhetg7fncv.brazilsouth.azurecontainer.io:8000/biology_api_app/questions/
```

POST endpoint: 'http://biology-api-app.cuggbpbhetg7fncv.brazilsouth.azurecontainer.io:8000/biology_api_app/answer/'
```bash
curl.exe -H "Content-Type: application/json" -d '{\"question_id\": \"6512e2b5fd7b465b02516710\", \"submitted_answer\": \"favorecem a adapta\u00e7\u00e3o de plantas lenhosas madeireiras.\"}' 'http://biology-api-app.cuggbpbhetg7fncv.brazilsouth.azurecontainer.io:8000/biology_api_app/answer/'
```

