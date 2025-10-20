from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()
Instrumentator().instrument(app).expose(app)

@app.get("/hello/{name}")
def hello_by_name(name: str):
    return {"message": f"Hello, {name}!"}

@app.get("/about")
def about():
    return {"message": "This is FastAPI application with CI/CD workflow useing local Docker image"}
