# debbugs-graphql

A GraphQL API server for the Debbugs bug tracking system. This project provides a modern GraphQL interface to query bug information from Debbugs instances like debbugs.gnu.org.

## Overview

debbugs-graphql wraps the Debbugs SOAP API with a GraphQL layer, making it easier to query bug statuses using standard GraphQL queries. Built with Strawberry GraphQL and FastAPI, it offers a familiar developer experience with an interactive GraphQL playground.

## Features

- Query single or multiple bug statuses in one request
- Full bug metadata including severity, tags, versions, and more
- Interactive GraphQL playground at `/graphql`
- Type-safe schema with Pydantic models

## Requirements

- Python 3.11 or later

## Installation

```bash
pip install -e .
```

For development:

```bash
pip install -e ".[dev]"
```

## Usage

Start the server:

```bash
debbugs-graphql
```

Options:

```
--host      Host to bind to (default: 127.0.0.1)
--port      Port to listen on (default: 8000)
--reload    Enable auto-reload for development
```

Once running, open http://localhost:8000/graphql in your browser to access the GraphQL playground.

## Example Queries

Get a single bug status:

```graphql
query {
  status(bugnumber: 12345) {
    bugNum
    subject
    severity
    package
    originator
    pending
    done
    tags
  }
}
```

Get multiple bug statuses:

```graphql
query {
  statuses(bugnumbers: [12345, 12346, 12347]) {
    bugNum
    subject
    severity
    package
  }
}
```

## Available Fields

The `Status` type includes:

| Field | Description |
|-------|-------------|
| `bugNum` | The bug number |
| `subject` | Subject/title of the bug report |
| `severity` | Bug severity level |
| `package` | Package name |
| `source` | Source package name |
| `originator` | Submitter of the bug report |
| `owner` | Person responsible for fixing |
| `done` | Maintainer who closed the bug (empty if open) |
| `pending` | Either "pending" or "done" |
| `date` | Date of bug creation |
| `lastModified` | Date of last update |
| `forwarded` | URL or email where bug was forwarded |
| `mergedwith` | Bugs this was merged with |
| `blockedby` | Bugs blocking this one |
| `blocks` | Bugs this one blocks |
| `tags` | Bug tags |
| `archived` | Whether the bug is archived |
| `affects` | Affected package names |
| `summary` | Arbitrary summary text |
| `fixedVersions` | Versions where the bug is fixed |
| `foundVersions` | Versions where the bug was found |

## License

Apache License 2.0
