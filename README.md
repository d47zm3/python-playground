# Python Playground

Collecting Code And Best Practices

## Setup

TODO: Cookie Cutter?

```
# bootstrap script with things below

bash <(curl -s https://d47zm3.me/python-bootstrap) # work in progress

# setup.py for humans
curl -O https://raw.githubusercontent.com/navdeep-G/setup.py/master/setup.py

# test setup.py
pip install -e .

# .gitignore
curl https://raw.githubusercontent.com/github/gitignore/master/Python.gitignore -o .gitignore

# new environment along with development dependencies
pipenv install --python python3.7 twine --dev

# this is for my neovim so it works inside pipenv
pipenv install neovim autopep8 flake8 isort pep8 pydocstyle pylint pytest-cov yapf black==19.10b0 jedi mypy --dev

# when there's problem with dependencies
pipenv lock --pre --clear
```

## Doc Tests (And Typing)
```python

from typing import List, Dict


class Results:

    def __init__(self, total_time: float, requests: List[Dict]):
        self.total_time = total_time
        self.requests = requests

    def slowest(self) -> float:
        """
        Returns the slowest request's completion time

        >>> results = Results(10.6, [{
        ...     'status_code': 200,
        ...     'request_time': 3.4
        ... }, {
        ...     'status_code': 500,
        ...     'request_time': 6.1
        ... }, {
        ...     'status_code': 200,
        ...     'request_time': 1.04
        ... }])
        >>> results.slowest()
        6.1
        """
        pass

python -m doctest assault/stats.py
```

## MyPy

```python
def greeting(name: str) -> str:
    return 'Hello ' + name

greeting(3)
greeting("Alice")
```

```
>>> mypy test.py
test.py:4: error: Argument 1 to "greeting" has incompatible type "int"; expected "str"
Found 1 error in 1 file (checked 1 source file)
```
