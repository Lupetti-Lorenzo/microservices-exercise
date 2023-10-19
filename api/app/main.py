import sys
from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from kubernetes import client, config
import os

# print(os.getenv("SECRET_KEY"))

# FASTAPI
app = FastAPI()

# K8 CONFIG
# config.load_kube_config()
# v1 = client.CoreV1Api()


class Rank(BaseModel):
    id: int
    rank: int
    # name: str
    # description: str | None = None
    # tags: list[str] = []


@app.get("/")
async def root():
    if sys.prefix == sys.base_prefix:
        print("Running in system-wide Python environment")
    else:
        print(f"Running in a virtual environment at {sys.prefix}")

    return {"message": "Hello World"}


@app.get("/rankings")
async def rankings() -> list[Rank]:
    return [{"id": 1, "rank": 10}, {"id": 2, "rank": 11}]


@app.get("/rankings/{id}")
async def rankings_id(id: int) -> Rank:
    return {"id": id, "rank": 10}


@app.post("/rankings")
async def create_rank(r: Rank) -> list[Rank]:
    return [{"id": 1, "rank": 10}, {"id": 2, "rank": 11}, r]


# @app.get("/pods")
# async def get_pods() -> list[str]:
#     ret = v1.list_pod_for_all_namespaces(watch=False)
#     return [pod.status.pod_ip for pod in ret.items if pod.status.pod_ip is not None]


@app.get("/error")
async def throw_error():
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="Item not found")