from tortoise import Tortoise, run_async

from fastapi_graphql.config.env_setting import settings


async def init():
    """
    初始化连接
    """
    #  also specify the app name of "models"
    #  which contain models from "app.models"
    await Tortoise.init(
        db_url=settings.orm_db_url,
        modules={"models": ["fastapi_graphql.model.models"]},
    )
    # Generate the schema
    await Tortoise.generate_schemas()


async def do_stuff():
    """关闭数据库"""
    await Tortoise.close_connections()


if __name__ == "__main__":
    run_async(init())  # 创建数据库
    run_async(do_stuff())  # 清理数据库连接
