# graphql_router.py
from typing import List, Optional
from fastapi import Depends
import strawberry
from strawberry.fastapi import GraphQLRouter

from fastapi_graphql.config.env_setting import settings
from fastapi_graphql.model.models import (
    User,
    User_orm,
    UserInput,
    UserType,
)
from fastapi_graphql.services.generic_services import UserService, get_user_service


@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "Hello World"

    @strawberry.field
    def all_user(
        self,
        service: UserService = Depends(get_user_service),
    ) -> Optional[List[UserType]]:
        return service.find_all_user()

    @strawberry.field
    def user(
        self,
        input_id: str,
        service: UserService = Depends(get_user_service),
    ) -> Optional[UserType]:
        return User_orm.from_queryset_single(User.get(id=input_id))


@strawberry.type
class UserMutation:
    @strawberry.mutation
    def save_user(
        self,
        user: UserInput,
        service: UserService = Depends(get_user_service),
    ) -> Optional[UserType]:
        return service.save_model(user)

    @strawberry.mutation
    def delete_user(
        self,
        pk_id: str,
        service: UserService = Depends(get_user_service),
    ) -> int:
        return service.del_model(pk_id)


schema = strawberry.Schema(Query, UserMutation)

# get:/graphql
graphql_app = GraphQLRouter(schema, graphiql=settings.graphiql)
