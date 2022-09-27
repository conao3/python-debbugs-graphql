import argparse
import uvicorn


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', default='127.0.0.1')
    parser.add_argument('--port', default=8000, type=int)
    parser.add_argument('--reload', action='store_true')
    args = parser.parse_args()

    uvicorn.run(
        "debbugs_graphql.main:app",
        **{
            key: getattr(args, key)
            for key in (
                'host',
                'port',
                'reload',
            )
        }
    )


if __name__ == '__main__':
    main()
