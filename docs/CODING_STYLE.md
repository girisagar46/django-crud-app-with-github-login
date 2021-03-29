## Coding style

This project uses [black](https://pypi.org/project/black/) coding style to maintain consistency and readability. Please install [pre-commit first](https://pre-commit.com/#quick-start) as discussed below.

## Install pre-commit

```bash
brew install pre-commit
pre-commit install
```

`pre-commit` is used to check the codebase has been formatted across the entire project.

First install [isort](https://github.com/timothycrosley/isort), [black](https://github.com/ambv/black) & [flake8](https://gitlab.com/pycqa/flake8) installed into your local machine. Any commits will trigger the pre-commit and warns you of unformatted code or errors before bringing those files to staging.

You can run those commands separately if you wish to (e.g. with black the command would look lik
e `black path/to/your/python/code.py` )

Some files are ignored, for example in the case of `.md` files. Also note that initial pre-commit will take a while at first. Please allow a few minutes for it to finish.

```bash
❯ gcmsg "fix: README"
[INFO] Initializing environment for https://github.com/timothycrosley/isort.
[INFO] Initializing environment for https://github.com/ambv/black.
[INFO] Initializing environment for https://gitlab.com/pycqa/flake8.
[INFO] Installing environment for https://github.com/timothycrosley/isort.
[INFO] Once installed this environment will be reused.
[INFO] This may take a few minutes...
[INFO] Installing environment for https://github.com/ambv/black.
[INFO] Once installed this environment will be reused.
[INFO] This may take a few minutes...
[INFO] Installing environment for https://gitlab.com/pycqa/flake8.
[INFO] Once installed this environment will be reused.
[INFO] This may take a few minutes...
isort................................................(no files to check)Skipped
black................................................(no files to check)Skipped
flake8...............................................(no files to check)Skipped
[main c286eb0] fix: README
 1 file changed, 6 insertions(+)
```
