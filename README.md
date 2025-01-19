# Sample Project

This project is intended to be a demonstration of a simple Python
API project that uses some modern Python build tooling.

## Prerequisites
The main prerequisite is that the [uv](https://docs.astral.sh/uv/) packaging tool 
is installed globally. Mac users can use 
```bash
brew install uv
```
For other installation paths, see the `uv` documentation.

The instructions that follow assume a *IX-style environment - e.g. Linux, Mac terminal or WSL.

## Basic Local Development Setup
Fork and clone this repository to your local machine. 

Assuming that `uv` is installed, just move to the root directory of the project and run:
```bash
source setup.sh
```
This will set up a virtual environment, install dependencies and create a documentation folder.

The script will make available a number of functions that can be run in the current shell:

- `build` - rebuild the project and documentation after a code change or the addition
 of a dependency
- `unit-test` - run the unit tests with verbose output and coverage
- `formatter` - run the [ruff](https://docs.astral.sh/ruff/) formatting tool
- `checker` - run the `ruff` linting check
- `sec-check` - run [pip-audit](https://pypi.org/project/pip-audit/) and 
[bandit](https://bandit.readthedocs.io/en/latest/) to assess code and dependencies 
for vulnerabilities
- `all-checks` - run all checks
- `run-app` - run the server locally

Simply type any of these into the command line to run them. Furthermore, any `uv` command can
be run separately.

## Local Execution

To run the (very simple) server locally, use:
```bash
run-app
```
and navigate to `localhost:8000/healthcheck` in your browser to check it is working.

## Development Pathway

A project like this can be created initially with the `uv init -app` command.

Then:
- modify the directory structure as required
- modify the `pyproject.toml` file as required, and include the `pythonpath` configuration for
`pytest` module discovery
- use the `uv add <library-name>` command for code dependencies or `uv add --dev <library-name>`
for development dependencies
- add and modify the `setup.sh` script ensuring it is saved as executable using the 
command `chmod +x setup.sh`


