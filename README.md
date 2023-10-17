# repow

## gang  

# How to start

## Install virtual enviroment
```bash
pip install pipenv
```

## Enter virtual enviroment
```bash
pipenv shell
```

## Install dependencies 
```bash
pip install -r requirements.txt
```

## Run the application
```bash
uvicorn main:app --reload --port 8000
```

## Added new dependency?
```bash
pip freeze > requirements.txt # and push the file to the repo
```

## Enviroment variables?
Create a .env file with key values like this: SECRET_KEY="HELLO NIBBA"
Pipenv will automatically detect it.
Get the variable: os.getenv("SECRET_KEY")
We will manually send the .env to each other for security. 