#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------ #
#
# Name: clean_all.py
# Purpose: clean oll of the Xfce repositories from
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

subprocess.call("clean_apps.py", shell=True)
subprocess.call("clean_bindings.py", shell=True)
subprocess.call("clean_core.py", shell=True)
subprocess.call("clean_panel_plugins.py", shell=True)
subprocess.call("clean_thunar_plugins.py", shell=True)
