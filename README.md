# repow

## gang  

# How to start 

## Without virtual env
```bash
pip install -r requirements.txt
```

## With virtual enviroment

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
pip freeze > requirements.txt # update requirements
```

## Run the application
```bash
uvicorn main:app --reload --port 8000
```

## Enviroment variables?

Create a .env file with key values like this: SECRET_KEY="HELLO NIBBA"

Pipenv will automatically detect it.

Get the variable: os.getenv("SECRET_KEY")

We will manually send the .env to each other for security. 