#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Set Docker Hub username and image name
DOCKER_USERNAME="Rigani Jegatheeswaran"
IMAGE_NAME="docker/dev-environments-default:stable-1"

# Build the Docker image
docker build -t $DOCKER_USERNAME/$IMAGE_NAME .

# Tag the Docker image with a version (e.g., using Git commit hash)
TAG=$(git rev-parse --short HEAD)
docker tag $DOCKER_USERNAME/$IMAGE_NAME $DOCKER_USERNAME/$IMAGE_NAME:$TAG

# Log in to Docker Hub
echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin

# Push the Docker image to Docker Hub
docker push $DOCKER_USERNAME/$IMAGE_NAME:$TAG
