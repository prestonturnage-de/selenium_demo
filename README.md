# Selenium Demo with CI/CD integration

This project spins up a standalone selenium chrome container in docker which then runs a python program to to run a couple of simple tests in selenium. When changes are pushed to this repository, github actions are used to automatically build a docker image and push it to github container registry.

For this project, I configured Black, iSort, and Flake8 - standard code quality tools for python.
Additionally, I configured pre-commit to ensure that code quality is maintained before each commit. This is important for CI/CD because when github actions run, the same pre-commit configuration is used to ensure that the code has been linted - helping to ensure that poor quality code is not merged with the repository.
