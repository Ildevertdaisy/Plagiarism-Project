
# file: projects/api/api.py

from projects.app import app


@app.get("/")
def index():
    return {"message": "Hello from Projects microservice"}