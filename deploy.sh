#!/bin/bash

# Define variables
imageName="your_image_name"
containerName="your_container_name"
resourceGroup="your_resource_group"
registryName="your_registry_name.azurecr.io"
port="8000"

# Build the Docker image
docker build -t $imageName .

# Authenticate with Azure Container Registry
az acr login --name $registryName

# Tag the image
docker tag $imageName $registryName/$imageName

# Push the image to Azure Container Registry
docker push $registryName/$imageName

# Deploy the image to Azure Container Instances
az container create \
  --resource-group $resourceGroup \
  --name $containerName \
  --image $registryName/$imageName \
  --dns-name-label $containerName \
  --ports $port \
  --ip-address public
