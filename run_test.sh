#! /bin/bash

echo "Building test container..."
docker compose build --no-cache

echo "Running tests..."
docker compose up

echo "Stopping selenium"
docker compose down
