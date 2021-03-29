## Prerequisite

First obtain your GitHub OAuth credentials by registering a GitHub OAuth app ([as described here](https://github.com/settings/applications/new)). When you have these make note of them somewhere first.

Next, generate a secret key for Django

```python
>>> from django.core.management.utils import get_random_secret_key
>>> print(get_random_secret_key())
>>> <your-generated-secret-key>
```

Then, as stated earlier, paste these values into your `.env.example` file

```bash
# .env.example
OAUTH_CLIENT_ID=<your-github-oauth-client-id>
OAUTH_CLIENT_SECRET=<your-github-oauth-secret>
SECRET_KEY=<your-generated-django-secret-key>
```

copy the file over as your `.env` file

```bash
cp -p .env.example .env
```

You are now ready to install the project dependencies

```bash
❯ python -m pip install -r requirements.txt
```

We also need to create a superuser for testing later. Make note of the password.

```bash
❯ python manage.py createsuperuser testuser
```
