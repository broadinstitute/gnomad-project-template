import os
import tempfile

import nox


@nox.session
def test_nox_in_new_project(session):
    session.install("cookiecutter")

    template_directory = os.getcwd()
    with tempfile.TemporaryDirectory() as temp_dir:
        session.cd(temp_dir)

        with open(os.path.join(temp_dir, "config.yaml"), "w") as config_file:
            config_file.write(
                'default_context:\n  project_name: "gnomAD project template test"\n'
            )
        session.run(
            "cookiecutter",
            "--no-input",
            "--config-file=config.yaml",
            template_directory,
        )
        session.cd(os.path.join(temp_dir, "gnomad_project_template_test"))

        session.install("nox")
        session.run("nox")


@nox.session
def test_precommit_hooks_in_new_project(session):
    session.install("cookiecutter")

    template_directory = os.getcwd()
    with tempfile.TemporaryDirectory() as temp_dir:
        session.cd(temp_dir)

        with open(os.path.join(temp_dir, "config.yaml"), "w") as config_file:
            config_file.write(
                'default_context:\n  project_name: "gnomAD project template test"\n'
            )
        session.run(
            "cookiecutter",
            "--no-input",
            "--config-file=config.yaml",
            template_directory,
        )
        session.cd(os.path.join(temp_dir, "gnomad_project_template_test"))

        session.run("git", "init", "-b", "main", external=True)
        session.run("git", "config", "user.email", "test@example.com", external=True)
        session.run("git", "config", "user.name", "a test script", external=True)
        session.install("pre-commit")
        session.run("pre-commit", "install")
        session.run("git", "add", ".", external=True)
        session.run("git", "commit", "-m", "Initial commit", external=True)


nox.options.sessions = [
    "test_nox_in_new_project",
    "test_precommit_hooks_in_new_project",
]
