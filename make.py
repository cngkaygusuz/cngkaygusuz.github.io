#!/usr/bin/env python
import os
import sys
import shutil

import jinja2


SRC_DIR = 'src'
TARGET_DIR = 'build'


def render():
    """Render templates."""
    # read from src, render, copy to build, within the same path
    # construct the index afterwards
    shutil.rmtree(TARGET_DIR, ignore_errors=True)

    loader = jinja2.FileSystemLoader('.')
    env = jinja2.Environment(loader=loader)

    for entry in os.walk(SRC_DIR):
        src_dir_path, _, filenames = entry
        
        target_dir = src_dir_path.replace(SRC_DIR, TARGET_DIR, 1)
        os.mkdir(target_dir, mode=0o755)
        
        for filename in filenames:
            source_file = os.path.join(src_dir_path, filename)
            target_file = os.path.join(target_dir, filename)
            template = env.get_template(source_file)
            
            rendered = template.render()

            with open(target_file, "w") as file_:
                file_.write(rendered)


def venv():
    """Set up local env for development."""
    os.system("sudo apt-get -y install virtualenv")
    os.system("virtualenv --no-site-packages -p /usr/bin/python3 venv/")
    os.system("PATH=venv/bin; pip install -r requirements.txt")


def print_usage():
    """Print usage string to stdout."""
    print("Usage: make.py ARG")
    print("")
    print("ARG=venv: create the virtual environment")
    print("ARG=render: render templates")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print_usage()
        sys.exit(1)

    arg = sys.argv[1]

    if arg == "render":
        render()
    elif arg == "venv":
        venv()
    else:
        print_usage()

