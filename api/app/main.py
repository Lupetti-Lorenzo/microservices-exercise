import sys
import logging
from fastapi import FastAPI, status, HTTPException, Request
from pydantic import BaseModel
from kubernetes import client, config
import os
import re
import random
import pika # RabbitMQ

# print(os.getenv("SECRET_KEY"))
## ----------------- SETUP ----------------- ##
# FASTAPI
app = FastAPI()



# K8 CONFIG
try:
    config.load_kube_config()
except:
    # load_kube_config throws if there is no config, but does not document what it throws, so I can't rely on any particular type here
    config.load_incluster_config()
v1 = client.CoreV1Api()  

## ----------------- MODELS ----------------- ##

class Rank(BaseModel):
    id: int
    rank: int
    # name: str
    # description: str | None = None
    # tags: list[str] = []

## ----------------- ROUTES ----------------- ##

@app.get("/")
async def root():
    if sys.prefix == sys.base_prefix:
        print("Running in system-wide Python environment")
    else:
        print(f"Running in a virtual environment at {sys.prefix}")

    return {"message": "Hello World"}

# RANKINGS
@app.get("/rankings")
async def rankings() -> list[Rank]:
    return [{"id": 1, "rank": 10}, {"id": 2, "rank": 11}]


@app.get("/rankings/{id}")
async def rankings_id(id: int) -> Rank:
    return {"id": id, "rank": 10}


@app.post("/rankings")
async def create_rank(r: Rank) -> list[Rank]:
    return [{"id": 1, "rank": 10}, {"id": 2, "rank": 11}, r]


# K8
@app.get("/pods")
async def get_pods() -> list[str]:
    pods = v1.list_namespaced_pod("default",watch=False).items
    return [pod.status.pod_ip for pod in pods if pod.status.pod_ip is not None]

@app.get("/pods/logs")
async def get_pods_logs(request: Request) -> dict[str,str]:
    # get all pods
    ret = v1.list_namespaced_pod("default",watch=False)
    pods_logs = {} # return item
    for pod in ret.items:  
            # extract name and logs from the pod
            name = pod.metadata.name
            logs = v1.read_namespaced_pod_log(name=name, namespace="default")
            # if the request specify to include health check i will not filter the logs
            if request.query_params.get("health") == None or request.query_params.get("health") == "false" :
                # Split the log string into individual lines
                log_lines = logs.split('\n')
                # Filter out log lines that contain the "/health" endpoint
                filtered_log_lines = [line for line in log_lines if "/health" not in line]
                # Join the filtered lines to reconstruct the log string
                logs = '\n'.join(filtered_log_lines)
                # Split the log string into individual lines
                log_lines = logs.split('\n')
                # Filter out log lines that contain the "/health" endpoint
                filtered_log_lines = [line for line in log_lines if "/health" not in line]
                # Join the filtered lines to reconstruct the log string
                logs = '\n'.join(filtered_log_lines)
            # add the logs to the dictionary
            pods_logs[name] = logs
    return pods_logs
	
@app.get("/clusterid")
async def get_current_pod_id() -> str:
  return (os.getenv("HOSTNAME") or "unknown") 


# HEALTH
@app.get("/health")
async def health_check() -> str:
	return "OK"

@app.get("/badHealth")
async def throw_error():
    raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail="Service unavailable")



# RABBITMQ 
 
# Connect to RabbitMQ ClusterIP service
connection = pika.BlockingConnection(pika.ConnectionParameters('rabbit-mq'))
channel = connection.channel()

# Create queue
channel.queue_declare(queue='hello')
# Send message to queue
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')

connection.close()



# OTHER