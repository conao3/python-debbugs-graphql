import uvicorn


def main():
    uvicorn.run("debbugs_graphql.main:app")


if __name__ == '__main__':
    main()
