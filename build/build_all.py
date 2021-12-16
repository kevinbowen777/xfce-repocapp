#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------ #
#
# Name: build_all.py
# Purpose: build oll of the Xfce repositories from
#           https://gitlab.xfce.org/
#
# version: 0.7.1
# updated: 20211207
# @author: kevin.bowen@gmail.com
#
# }}} ------------------------------------------------------------------ #

import os
import subprocess

os.chdir(os.path.dirname(os.path.realpath(__file__)))

subprocess.call("build_apps.py", shell=True)
subprocess.call("build_bindings.py", shell=True)
subprocess.call("build_core.py", shell=True)
subprocess.call("build_panel_plugins.py", shell=True)
subprocess.call("build_thunar_plugins.py", shell=True)
