## Coding style

This project uses [black](https://pypi.org/project/black/) coding style to maintain consistency and readability. Please install [pre-commit first](https://pre-commit.com/#quick-start) as discussed below.

## Install pre-commit

`pre-commit` is used to check the codebase has been formatted across the entire project.

First install [isort](https://github.com/timothycrosley/isort), [black](https://github.com/ambv/black) & [flake8](https://gitlab.com/pycqa/flake8) installed into your local machine. Any commits will trigger the pre-commit and warns you of unformatted code or errors before bringing those files to staging.

You can run those commands separately if you rish to (e.g. with black the command would look like `black path/to/your/python/code.py` )
