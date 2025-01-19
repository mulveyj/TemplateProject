#!/bin/bash

CODE_FOLDER='src'
TEST_FOLDER='test'

build () {
    uv sync
    uv run pdoc src/app -o ./docs
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
    uv run bandit src
}

all-checks () {
    formatter
    checker
    unit-test
    sec-check
}

build
