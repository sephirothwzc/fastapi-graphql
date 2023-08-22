# env_setting.py

from typing import Optional
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    env-系统设置

    Args:
        BaseSettings (_type_): _description_

    Attributes:
        app_name (str): 项目名称，默认为 "fastapi-graphql"。
        admin_email (str): 管理员邮箱，默认为 "zhanchao.wu@icloud.com"。
        port (Optional[int]): 服务器端口号，如果未提供则为 None。
        items_per_user (int): 每个用户允许的项目数量，默认为 50。
    """

    app_name: str = "fastapi-graphql"  # 项目名称
    admin_email: str = "zhanchao.wu@icloud.com"  # 邮箱
    port: Optional[int] = None
    items_per_user: int = 50
