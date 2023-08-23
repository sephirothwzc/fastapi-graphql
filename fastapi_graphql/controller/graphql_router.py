# graphql_router.py
import strawberry
from strawberry.fastapi import GraphQLRouter

from fastapi_graphql.config.env_setting import settings


@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "Hello World"


schema = strawberry.Schema(Query)

# get:/graphql
graphql_app = GraphQLRouter(schema, graphiql=settings.graphiql)
