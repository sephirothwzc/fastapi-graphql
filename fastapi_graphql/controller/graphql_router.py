# graphql_router.py
from typing import List, Optional
import strawberry
from strawberry.fastapi import GraphQLRouter

from fastapi_graphql.config.env_setting import settings
from fastapi_graphql.model.models import (
    User,
    User_orm,
    UserInput,
    UserType,
)
from fastapi_graphql.services.generic_services import UserService


@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "Hello World"

    @strawberry.field
    def all_user() -> Optional[List[UserType]]:
        return User_orm.from_queryset(User.all())

    @strawberry.field
    def user(self, input_id: str) -> Optional[UserType]:
        return User_orm.from_queryset_single(User.get(id=input_id))


@strawberry.type
class UserMutation:
    @strawberry.mutation
    def save_user(
        self,
        user: UserInput,
    ) -> Optional[UserType]:
        return UserService().save_model(user)


schema = strawberry.Schema(Query, UserMutation)

# get:/graphql
graphql_app = GraphQLRouter(schema, graphiql=settings.graphiql)
