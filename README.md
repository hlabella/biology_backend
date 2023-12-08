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

3. Open `https://localhost:8000` in the browser

## Dockerhub Image:

You can pull my image from: https://hub.docker.com/repository/docker/hlabellacosta/biology-api-app-repository/general

```bash
docker pull hlabellacosta/biology-api-app-repository:latest
```

Then run the container:

```bash
docker run -d --name biology-api-app-repository -p 8000:8000 hlabellacosta/biology-api-app-repository:latest
```


### Accessing the Application

GET /questions endpoint: 
```bash
https://localhost:8000/biology_api_app/questions/
```

POST /answer endpoint: 
```bash
https://localhost:8000/biology_api_app/answer/
```

### Try it:

To try the GET /questions endpoint, try:
```bash
curl http://localhost:8000/biology_api_app/questions/
```

To try the Post /answer endpoint, try:
```bash
curl http://localhost:8000/biology_api_app/questions/
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
Steps to Deploy
Open Terminal or Command Prompt:
Navigate to your project's root directory where the deploy.sh script is located.

Make the Script Executable (if on Unix/Linux/Mac):
chmod +x deploy.sh

Execute the script by typing:
./deploy.sh

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

http://biology-api-app.cuggbpbhetg7fncv.brazilsouth.azurecontainer.io:8000/biology_api_app/questions/
http://biology-api-app.cuggbpbhetg7fncv.brazilsouth.azurecontainer.io:8000/biology_api_app/answer/

