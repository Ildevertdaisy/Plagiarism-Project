
from extractor.app import app
from pydantic import BaseModel
from .logic import extract_text_from_zip


class InputSchema(BaseModel):
    file_token: str


class OuputSchema(BaseModel):
    text: str


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


@app.post("/extractor/text", response_model=OuputSchema)
def extract_text(payload: InputSchema):
    file_token = payload.file_token
    output = extract_text_from_zip(file_token)
    return {
        "text": output
    }