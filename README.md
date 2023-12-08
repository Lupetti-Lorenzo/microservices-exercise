<div align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/3/39/Kubernetes_logo_without_workmark.svg" alt="Kubernetes Logo" width="160">
  <h1>Microservices Exercise</h1>
	<p></p>
</div>
<br>

## 🚀 Features

- ***WebApplication*** in SvelteKit
- ***REST API*** in pyton FastApi
- ***RabbitMQ*** broker deployed via kubectl
- ***Dockerfile*** files for building the apps
- ***deployment*** folder with all the necessary to deploy the applications in a ***kubernetes*** cluster and allow communication between them
- All tested in my PC using tools like ***docker*** for building, ***minikube*** for local deployment and ***k9s*** for monitoring and interacting with the cluster.
- ***UML*** diagrams to illustrate the system's structure


## 💻 Tech & Stuff used for this project 

![Docker](https://img.shields.io/badge/Docker-%232496ED.svg?style=for-the-badge&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-%23326CE5.svg?style=for-the-badge&logo=kubernetes&logoColor=white)
![YAML](https://img.shields.io/badge/YAML-%23000000.svg?style=for-the-badge&logo=yaml&logoColor=white)
![RabbitMQ](https://img.shields.io/badge/RabbitMQ-%23FF6600.svg?style=for-the-badge&logo=rabbitmq&logoColor=white)

![TypeScript](https://img.shields.io/badge/typescript-%23007ACC.svg?style=for-the-badge&logo=typescript&logoColor=white)
![Svelte Kit](https://img.shields.io/badge/Svelte%20Kit-%23FF3E00.svg?style=for-the-badge&logo=svelte&logoColor=white)
![npm](https://img.shields.io/badge/npm-%23000000.svg?style=for-the-badge&logo=npm&logoColor=white)

![Python](https://img.shields.io/badge/Python-%233776AB.svg?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-%23007ACC.svg?style=for-the-badge&logo=fastapi&logoColor=white)
![OpenAPI](https://img.shields.io/badge/OpenAPI-%2361DAFB.svg?style=for-the-badge&logo=openapi-initiative&logoColor=white)

![UML](https://img.shields.io/badge/UML-%23000000.svg?style=for-the-badge&logo=uml&logoColor=white)


# API

## How to start

### Install dependencies

```bash
pip install -r requirements.txt
```

### Add new package

```bash
pip install package_name
pip freeze > requirements.txt
```

## How to start - pipenv

### Create virtual enviroment

```bash
cd api
pipenv shell
```

### Install dependencies from Pipfile

```bash
pipenv install -r requirements.txt
```

### Add new packages 

```bash
pipenv install package_name
pip freeze > requirements.txt
```

## Run the application
```bash
uvicorn app.main:app --reload --port 8000
```

## Enviroment variables?

Create a .env file with key values like this: SECRET_KEY="HELLO NIBBA".

Pipenv will automatically detect it.

Get the variable: os.getenv("SECRET_KEY")

We will manually send the .env to each other for security. 

# Frontend

## How to start

### Install dependencies

```bash
npm install
```

## Run the application

```bash
npm run dev
```
## Add new packages

```bash
npm install package_name
```

# Local Deployment

I assume that you have docker, minikube and kubectl installed and working on your local machine.

All commands shown are executed from the root folder.

## Build Apps

Build the images for each microservice in the project.

```bash
docker build --no-cache -t api:latest /api
docker build --no-cache -t frontend:latest /frontend
```

### Add the images to minikube

```bash
minikube image load api:latest # minikube image rm api - for removing
minikube image load frontend:latest
```

### Deploy

Add the RabbitMQ Cluster Operator.

```bash
kubectl apply -f https://github.com/rabbitmq/cluster-operator/releases/latest/download/cluster-operator.yml
```

Apply all the deployment files inside the folder deployment.

```bash
kubectl apply -f deployment/
```

### Testing

Right now you cannot access the services inside the cluster, use **minikube service** to create a port-forward and get access to the front end via localhost.

```bash
minikube service frontend-service
```


# UML 

## Component and Connector

This view shows how each service communicates with each other.

![](static/CeC.png)

## Sequences

### Getting index.html from the web-server

![](static/GetWebsite.png)

### Publishing a message to the broker

![](static/PublishMessage.png)

### Request a message from the broker

![](static/GetMessage.png)
