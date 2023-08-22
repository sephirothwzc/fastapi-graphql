# from typing import Union
from tortoise.contrib.fastapi import register_tortoise
from fastapi import FastAPI

from fastapi_graphql.config.env_setting import settings
from fastapi_graphql.controller import auth
from fastapi_graphql.orm.db import do_stuff, init

from .model.vo import HelloWord

app = FastAPI(title=settings.app_name)

register_tortoise(
    app,
    db_url=settings.orm_db_url,
    modules={"models": ["fastapi_graphql.model.models"]},
)

# @lru_cache
# def get_settings():
#     return Settings()


# 依赖注入
# @app.get("/info")
# async def info(settings: Annotated[Settings, Depends(get_settings)]) -> Settings:
#     return {
#         "app_name": settings.app_name,
#         "admin_email": settings.admin_email,
#         "items_per_user": settings.items_per_user,
#     }

app.include_router(auth.routers, prefix="/auth")


# region app event
@app.on_event("startup")
async def startup_event():
    """添加在应用程序启动之前运行初始化数据库"""
    await init()


@app.on_event("shutdown")
async def shutdown_event():
    """添加在应用程序关闭时关闭所有数据库链接"""
    await do_stuff()


# endregion


# region restful
@app.get("/")
async def read_root() -> HelloWord:
    """
    hello word

    Returns:
        HelloWord: _description_
    """
    return {"Hello": "World"}


# endregion
