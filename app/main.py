from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def hello():
    return {"message": "Hello from CI/CD!"}

@app.get("/bonjour")
def hello_test():
    return {"message": "Bonjour from CI/CD!"}

@app.get("/root")
def hello_test():
    return {"message": "Root route"}
