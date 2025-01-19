#!/bin/bash

CODE_FOLDER='src'
TEST_FOLDER='test'
ENTRYPOINT='app'

build () {
    uv sync
    uv run pdoc ${CODE_FOLDER}/${ENTRYPOINT} -o ./docs
}

unit-test () {
    uv run pytest -vrrP --testdox --cov ${CODE_FOLDER} ${TEST_FOLDER}
}

formatter () {
    uv run ruff format
}

checker () {
    uv run ruff check --fix
}

sec-check () {
    uv run pip-audit
    uv run bandit ${CODE_FOLDER}
}

all-checks () {
    formatter
    checker
    unit-test
    sec-check
}

run-app () {
    uv run fastapi dev ${CODE_FOLDER}/${ENTRYPOINT}.py
}

build
