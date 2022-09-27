from __future__ import annotations

import strawberry
import strawberry.experimental.pydantic

from . import client
from . import types

@strawberry.type
class Book:
    title: str
    author: str

    @classmethod
    def get_books(cls):
        return [
            Book(
                title='The Great Gatsby',
                author='F. Scott Fitzgerald',
            ),
        ]


@strawberry.experimental.pydantic.type(model=types.Status, all_fields=True)
class Status:
    log_modified: strawberry.auto = strawberry.field(deprecation_reason='deprecated')
    keywords: strawberry.auto = strawberry.field(deprecation_reason='deprecated')
    fixed_date: strawberry.auto = strawberry.field(deprecation_reason='deprecated')
    found_date: strawberry.auto = strawberry.field(deprecation_reason='deprecated')
    id: strawberry.auto = strawberry.field(deprecation_reason='deprecated')
    found: strawberry.auto = strawberry.field(deprecation_reason='deprecated')
    fixed: strawberry.auto = strawberry.field(deprecation_reason='deprecated')


@strawberry.type
class Query:
    @strawberry.field
    def status(self, bugnumber: int) -> Status:
        res = client.client.get_status(bugnumber)
        return Status.from_pydantic(res)

    @strawberry.field
    def statuses(self, bugnumbers: list[int]) -> list[Status]:
        res = client.client.get_statuses(bugnumbers)
        return [Status.from_pydantic(x) for x in res]


schema = strawberry.Schema(query=Query)
