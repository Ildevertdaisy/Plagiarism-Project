
from extractor.app import app
from pydantic import BaseModel


class InputSchema(BaseModel):
    file_token: str


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


@app.post("/extractor/text")
def extract_text(payload: InputSchema):
    pass