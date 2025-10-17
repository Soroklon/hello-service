from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    Instrumentator().instrument(app).expose(app)
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/hello")
def hello():
    return {"message": "Hello from CI/CD!"}

@app.get("/hello/{name}")
def hello_by_name(name: str):
    return {"message": f"Hello, {name}!"}

@app.get("/bonjour")
def hello_test():
    return {"message": "Bonjour from CI/CD!"}

@app.get("/root")
def hello_test():
    return {"message": "Root endpoint"}

@app.get("/about")
def about():
    return {"message": "This is FastAPI application with CI/CD workflow useing local Docker image"}
