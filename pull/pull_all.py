#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------ #
#
# Name: pull_all.py
# Purpose: update oll of the local Xfce repositories pulled from
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

subprocess.call("pull_apps.py", shell=True)
subprocess.call("pull_bindings.py", shell=True)
subprocess.call("pull_core.py", shell=True)
subprocess.call("pull_panel_plugins.py", shell=True)
subprocess.call("pull_thunar_plugins.py", shell=True)
subprocess.call("pull_www.py", shell=True)
