# from typing import Union
from functools import lru_cache
from typing import Annotated

from fastapi import Depends, FastAPI

from fastapi_graphql.config.env_setting import Settings

from .model.vo import HelloWord

app = FastAPI()


@lru_cache
def get_settings():
    return Settings()


@app.get("/")
async def read_root() -> HelloWord:
    """
    hello word

    Returns:
        HelloWord: _description_
    """
    return {"Hello": "World"}


@app.get("/info")
async def info(settings: Annotated[Settings, Depends(get_settings)]) -> Settings:
    return {
        "app_name": settings.app_name,
        "admin_email": settings.admin_email,
        "items_per_user": settings.items_per_user,
    }
