"""Nox sessions - xfce-repocapp"""

import tempfile

import nox

PYTHON_VERSIONS = ["3.10", "3.11", "3.12", "3.13"]
nox.options.sessions = "lint", "coverage", "tests"
locations = (
    "src",
    "./noxfile.py",
    # "docs/conf.py",
)


def install_with_constraints(session, *args, **kwargs):
    """Install packages constrained by Poetry's lock file.

    This function is a wrapper for nox.sessions.install. It
    invokes pip to install packages inside of the session's virtualenv.
    Additionally, pip is passed a constraints file generated from
    Poetry's lock file, to ensure that the packages are pinned to the
    versions specified in poetry.lock. This allows you to manage the
    packages as Poetry development dependencies.

    Arguments:
        session: The Session object.
        args: Command-line arguments for pip.
        kwargs: Additional keyword arguments for Session.install.
    """
    with tempfile.NamedTemporaryFile() as requirements:
        session.run(
            "poetry",
            "export",
            "--with",
            "dev",
            "--format=requirements.txt",
            "--without-hashes",
            f"--output={requirements.name}",
            external=True,
        )
        session.install(f"--requirement={requirements.name}", *args, **kwargs)


@nox.session(python=PYTHON_VERSIONS)
def coverage(session):
    """Build JSON coverage report."""
    install_with_constraints(session, "coverage")
    session.run("coverage", "run", "-p", "-m", "pytest")
    session.run("coverage", "combine")
    session.run("coverage", "report", "-m", "--skip-covered")
    session.run("coverage", "json", "-o", "htmlcov/coverage.json")
    session.run("coverage", "html")


@nox.session(python=PYTHON_VERSIONS)
def docs(session):
    """Build the documentation."""
    install_with_constraints(session, "sphinx")
    session.run("sphinx-build", "docs", "docs/_build")


@nox.session(python=PYTHON_VERSIONS)
def lint(session):
    """Lint using ruff."""
    args = session.posargs or locations
    install_with_constraints(
        session,
        "ruff",
    )
    session.run("ruff", "check", ".", *args)


@nox.session(python=PYTHON_VERSIONS)
def tests(session):
    """Run the test suite."""
    args = session.posargs
    with tempfile.NamedTemporaryFile() as requirements:
        session.run(
            "poetry",
            "export",
            "--format=requirements.txt",
            "--without-hashes",
            f"--output={requirements.name}",
            external=True,
        )
        session.install("-r", f"{requirements.name}")
    # session.run("poetry", "install", "--no-dev", external=True)
    install_with_constraints(
        session,
        "coverage[toml]",
        "pytest",
        "pytest-cov",
    )
    # session.run("pytest", *args)
    session.run(
        "python",
        "-Wonce::DeprecationWarning",
        "-Im",
        "pytest",
        *args,
    )
