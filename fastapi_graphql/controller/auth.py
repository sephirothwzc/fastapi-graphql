from typing import List
from fastapi import APIRouter

from fastapi_graphql.model.models import User, User_orm

routers = APIRouter()


@routers.get("/users")
async def get_users() -> List[User_orm]:
    return await User_orm.from_queryset(User.all())  # 查所有
