# repow

# API

## How to start 

### Install pipenv
```bash
pip install pipenv
```

### Enter virtual enviroment
```bash
pipenv shell
```

### Install dependencies from Pipfile
```bash
pipenv install
```

### Add new packages 
```bash
pipenv install [package] # install the package
```

## Run the application
```bash
uvicorn main:app --reload --port 8000
```

## Enviroment variables?

Create a .env file with key values like this: SECRET_KEY="HELLO NIBBA".

Pipenv will automatically detect it.

Get the variable: os.getenv("SECRET_KEY")

We will manually send the .env to each other for security. 

## Deployment

### Build

```bash
docker build --no-cache -t api:latest .
```

### Add the image to minikube cache
```bash
minikube cache add api:latest
# minikube cache reload - for refreshing the cache
```

### Deploy
```bash
kubectl apply -f deployment.yml
minikube service api-service # for testing
```