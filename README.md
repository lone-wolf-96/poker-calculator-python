# [Poker Calculator in Python](https://github.com/lone-wolf-96/poker-calculator-python/)

A demo that 'calculates' the winning poker hand between 2 players through algorithms.
This is the Python version of:

* [Poker Calculator in Java](https://github.com/lone-wolf-96/poker-calculator-java/)
* [Poker Calculator in C#](https://github.com/lone-wolf-96/poker-calculator-csharp/)
* [Poker Calculator in JavaScript](https://github.com/lone-wolf-96/poker-calculator-js/)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.
Probably needed: [Getting Started with Python in VS Code](https://code.visualstudio.com/docs/python/python-tutorial).

### Installation

It requires no other installation than having Python 3 latest stable release (3.7.3 by this date).

### Built with

* [Visual Studio Code](https://code.visualstudio.com/) was the code editor harnessed for this, it requires extensions from [Python](https://code.visualstudio.com/docs/languages/python) - <https://marketplace.visualstudio.com/items?itemName=ms-python.python>, and I essentially used [Python Extension Pack](https://marketplace.visualstudio.com/items?itemName=donjayamanne.python-extension-pack).

* [Pipenv](https://docs.pipenv.org/en/latest/) was used to setup and manage virtual environments and packages installations.

### Usage

The process is simple, once is run, it will ask for the pokerdata.txt source directory and then, for the poker_results.txt target directory (pokerdata.txt was added as an example for file format).

Unit tests are included.

These other articles might be helpful: [How to manage your Python projects with Pipenv](https://thoughtbot.com/blog/how-to-manage-your-python-projects-with-pipenv) and [Migrating from pip + virtualenv to Pipenv](https://blog.tecladocode.com/migrating-from-pip-virtualenv-to-pipenv/).

### Bear-in-mind

There may be some complications cause of Python Extension, such as unresolved imports or else.
So, this options in the generated settings.json file could be helpful:

```json
"python.analysis.disabled": [
        "unresolved-import",
        "undefined-variable"
]
```

For linting: [Pylint](https://www.pylint.org/), [Flake8](http://flake8.pycqa.org) and [PEP 8](https://pypi.org/project/pep8/) were used.

```json
"python.linting.pylintEnabled": true,
"python.linting.flake8Enabled": true,
"python.linting.pep8Enabled": true
```

And for testing: [Pytest](https://pytest.org/)

```json
"python.testing.pyTestEnabled": true
```

Other ways to run/debug is up to you.

## Authors

* **LoneWolf96** - *Final work* - [lone-wolf-96](https://github.com/lone-wolf-96/)

## Contributing

All sorts of suggestions are welcome. This has academic purposes only.

## License

This project is licensed under the [GNU General Public License v3.0](https://choosealicense.com/licenses/gpl-3.0/).
