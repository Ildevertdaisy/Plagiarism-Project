
from extractor.app import app


@app.get("/")
def index():
    return {
        "message": "Hello from Text extraction microservice"
    }


@app.get("/about")
def about():
    return {
        "developers" : [
            {
                "Developer": "Axel kolo",
            },
            {
                "Developer": "Ildevert Daisy MBOUNGOU"
            }
        ]
            
    }