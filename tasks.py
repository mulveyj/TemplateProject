from invoke import task

SOURCE_FOLDER = "src"
TEST_FOLDER = "test"


@task
def initialise(c):
    c.run("uv sync")


@task
def unit_tests(c, verbose=True, testdox=True, coverage=True):
    options = []
    if verbose:
        options.append("-vrrP")
    if testdox:
        options.append("--testdox")
    if coverage:
        options.append(f"--cov {SOURCE_FOLDER} {TEST_FOLDER}")
    cmd = f"uv run pytest {' '.join(options)}"
    c.run(cmd, echo=True)


@task
def security_tests(c, deps=True, code_check=True):
    if deps:
        c.run("uv run pip-audit")
    if code_check:
        c.run("uv run bandit src")


@task
def format_tests(c, formatyn=True, check=True):
    if formatyn:
        c.run("uv run ruff format")
    if check:
        c.run("uv run ruff check --fix")


@task
def generate_docs(c):
    c.run("uv run pdoc src/app -o ./docs")


@task
def prep(c):
    initialise(c)
    generate_docs(c)


@task
def all_checks(c):
    format_tests(c)
    unit_tests(c)
    security_tests(c)
