# gnomAD project template

[Cookiecutter](https://cookiecutter.readthedocs.io/) template for gnomAD projects.

This template sets up a Python project with:

- [Nox](https://nox.thea.codes/) for managing Python environments.
- [Black](https://black.readthedocs.io/) for code formatting.
- [isort](https://pycqa.github.io/isort/) for sorting imports.
- [pydocstyle](https://www.pydocstyle.org/) for docstring conventions.
- [Pre-commit hooks](https://pre-commit.com/) to run Black and pydocstyle.
- [Pylint](https://www.pylint.org/) for static analysis.
- [pytest](https://pytest.org/) for tests.
- [Sphinx](https://www.sphinx-doc.org/) for generating documentation.
- [GitHub Actions](https://github.com/features/actions) workflows for...
  - Running checks on PRs
  - Publishing documentation to [GitHub Pages](https://pages.github.com/).

## Getting started

- [Install cookiecutter](https://cookiecutter.readthedocs.io/en/latest/installation.html).

- Generate the project directory. Enter a project name when prompted.

  To clone the template repository using HTTPS, use:

  ```
  cookiecutter gh:broadinstitute/gnomad-project-template
  ```

  Note that this requires a [personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) in place of a password.

  Or, to clone the template repository using SSH, use:

  ```
  cookiecutter git@github.com:broadinstitute/gnomad-project-template.git
  ```

  For more information about cloning using HTTPS vs SSH, see ["About remote repositories"](https://docs.github.com/en/get-started/getting-started-with-git/about-remote-repositories).

### GitHub repository settings

To make full use of the [GitHub Actions](https://github.com/features/actions) workflows defined in the template, configure these settings in the project's GitHub repository.

- Create a [branch protection rule](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/defining-the-mergeability-of-pull-requests/about-protected-branches) for the `main` branch.

  - Require pull requests.
  - Enable [required status checks](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/defining-the-mergeability-of-pull-requests/about-protected-branches#require-status-checks-before-merging). Require the `Checks` and `Build documentation` status checks.

- On each commit to the `main` branch, documentation is automatically built and pushed to the `gh-pages` branch. To make the documentation available through [GitHub Pages](https://pages.github.com/), [configure GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site) to publish from the root of the `gh-pages` branch. Note that GitHub Pages websites are always public, even if the repository is private.
