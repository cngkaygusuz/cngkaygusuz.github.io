#!/usr/bin/env python
import os

import jinja2


def render():
    """Render templates."""
    # read from src, render, copy to build, within the same path
    loader = jinja2.FileSystemLoader(['src/', 'templates/'])
    env = jinja2.Environment(loader=loader)


    template = env.get_template("index.html")
    print(template.render())


def venv():
    """Set up local env for development."""
    os.system("sudo apt-get -y install virtualenv")
    os.system("virtualenv --no-site-packages -p /usr/bin/python3 venv/")
    os.system("PATH=venv/bin; pip install -r requirements.txt")

render()
