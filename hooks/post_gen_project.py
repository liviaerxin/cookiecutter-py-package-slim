#!/usr/bin/env python
import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    filepath = os.path.join(PROJECT_DIRECTORY, filepath)
    os.remove(filepath) if os.path.exists(filepath) else None


if __name__ == "__main__":
    if "{{ cookiecutter.create_author_file }}" != "y":
        remove_file("AUTHORS.rst")

    if "no" in "{{ cookiecutter.command_line_interface|lower }}":
        cli_file = os.path.join("{{ cookiecutter.project_slug }}", "cli.py")
        remove_file(cli_file)

    if "Not open source" == "{{ cookiecutter.open_source_license }}":
        remove_file("LICENSE")

    if "{{ cookiecutter.packaging }}" != "pip":
        remove_file("requirements.txt")

    if "{{ cookiecutter.packaging }}" != "poetry":
        remove_file("poetry.lock")
