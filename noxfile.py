from multiprocessing import cpu_count

from nox import Session
from nox import options
from nox import session


options.reuse_existing_virtualenvs = True
options.error_on_missing_interpreters = True
options.error_on_external_run = True


@session(python=["3.7"])
def lint(session: Session) -> None:
    session.install("black")
    _ = session.run("black", "--check", "-q", "src")
    session.install("isort")
    _ = session.run("isort", "--check", "src")
    session.install(
        "flake8",
        "flake8-absolute-import",
        "flake8-annotations",
        "flake8-bandit",
        "flake8-bugbear",
        "flake8-comprehensions",
        "flake8-debugger",
        "flake8-eradicate",
        "flake8-no-pep420",
        "flake8-pie",
        "flake8-print",
        "flake8-simplify",
        "flake8-unused-arguments",
    )
    _ = session.run("flake8", "src")


@session(python=["3.7", "3.8", "3.9", "3.10"])
def tests(session: Session) -> None:
    session.install("pytest", "pytest-cov", "pytest-xdist")
    n = max(round(cpu_count() / 2), 1)
    _ = session.run("pytest", f"-n={n}")
