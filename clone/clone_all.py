#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------ #
#
# Name: clone_all.py
# Purpose: clone oll of the Xfce repositories from
#           https://gitlab.xfce.org/
#
# version: 0.7
# updated: 20211207
# @author: kevin.bowen@gmail.com
#
# }}} ------------------------------------------------------------------ #

import os
import subprocess

os.chdir(os.path.dirname(os.path.realpath(__file__)))

subprocess.call("clone_apps.py", shell=True)
subprocess.call("clone_bindings.py", shell=True)
subprocess.call("clone_core.py", shell=True)
subprocess.call("clone_panel_plugins.py", shell=True)
subprocess.call("clone_thunar_plugins.py", shell=True)
subprocess.call("clone_www.py", shell=True)
