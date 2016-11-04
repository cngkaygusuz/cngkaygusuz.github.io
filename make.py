#!/usr/bin/env python
import os


def _exec():
    pass


def render():
    pass


def venv():
    os.system("sudo apt-get -y install virtualenv")
    os.system("virtualenv --no-site-packages -p /usr/bin/python3 venv/")

venv()
