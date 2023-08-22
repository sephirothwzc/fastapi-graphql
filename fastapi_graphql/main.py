# from typing import Union
from fastapi import FastAPI

from .model.vo import HelloWord

app = FastAPI()


@app.get("/")
async def read_root() -> HelloWord:
    return {"Hello": "World"}
