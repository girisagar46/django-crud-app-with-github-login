## Prerequisite

First obtain your GitHub OAuth credentials by registering a GitHub OAuth app ([as described here](https://github.com/settings/applications/new)). Make sure to set the **Authorization callback URL** as `http://localhost:8080/oauth/complete/github/`. When you have these make note of them somewhere first.

Install the project dependencies

```shell
$ python -m pip install -r requirements.txt
```

Next, generate a secret key for Django using Django shell

```shell
$ python manage.py shell
...
>>> from django.core.management.utils import get_random_secret_key
>>> get_random_secret_key()
<your-generated-secret-key>
>>> exit() # exit from the shell
```

Copy the file `.env.example` over as your `.env` file

```shell
$ cp -p .env.example .env
```

Then, as stated earlier, paste these values into your `.env` file

```shell
# .env
OAUTH_CLIENT_ID=<your-github-oauth-client-id>
OAUTH_CLIENT_SECRET=<your-github-oauth-secret>
SECRET_KEY=<your-generated-django-secret-key>
```

## Make migrations

```shell
$ python manage.py makemigrations personalprofile && python manage.py migrate
```

We also need to create a superuser for testing later. Make note of the password.

```shell
$ python manage.py createsuperuser --username testuser
```
