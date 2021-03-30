## Basic personal profile CRUD app with GitHub SSO login

An app that allows you to create/read/update/delete a personal profile information after logging in via GitHub.

## Prerequisites

This app requires a few steps to get started. [Read this doc first](./docs/PREREQUISITE.md) before jumping onto running it

## Running the app

After installing the dependencies from the prerequisites, run the local server:

```bash
❯ python manage.py runserver 8080
```

Then access http://localhost:8080 through the browser

**Please read [this doc](./docs/PROGRAM_FLOW.md) to understand the program flow**

## Unit tests

※ Please remember to have your testuser already created as described [in the prerequisite](./docs/PREREQUISITE.md).

```bash
❯ python manage.py test
```

# Install pre-commit

Discussed in detail in [this doc](./docs/CODING_STYLE.md)

refs: https://pre-commit.com/#quick-start
