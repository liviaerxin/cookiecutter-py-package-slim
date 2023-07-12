#!/usr/bin/env python
import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def delete(path, ignore_exist=True):
    """path could either be relative or absolute. """
    # check if file or directory exists
    if os.path.isfile(path) or os.path.islink(path):
        # remove file
        os.remove(path)
    elif os.path.isdir(path):
        # remove directory and all its content
        shutil.rmtree(path)
    else:
        if ignore_exist:
            return
        else:
            raise ValueError(f"Path {path} is not a file or dir.")
    
def remove_file(filepath):
    filepath = os.path.join(PROJECT_DIRECTORY, filepath)
    delete(filepath)
    
def remove_dir(dirpath):
    dirpath = os.path.join(PROJECT_DIRECTORY, dirpath)
    delete(dirpath)
    
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
        
    if "{{ cookiecutter.add_github_actions|lower }}" != "y":
        remove_dir(".github")
