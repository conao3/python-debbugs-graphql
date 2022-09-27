import strawberry


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


@strawberry.type
class Query:
    books: list[Book] = strawberry.field(resolver=Book.get_books)


schema = strawberry.Schema(query=Query)
