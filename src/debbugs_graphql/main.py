import strawberry
import strawberry.fastapi
import fastapi

from . import schema_graphql

app = fastapi.FastAPI()

graphql_app = strawberry.fastapi.GraphQLRouter(schema_graphql.schema)
app.include_router(graphql_app, prefix="/graphql")
