
# file : projects/app.py
from fastapi import FastAPI

app = FastAPI(debug=True)

from projects.api import api