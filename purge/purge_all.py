#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------ #
#
# Name: purge_all.py
# Purpose: delete oll of the local Xfce repositories pulled from
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

subprocess.call("purge_apps.py", shell=True)
subprocess.call("purge_bindings.py", shell=True)
subprocess.call("purge_core.py", shell=True)
subprocess.call("purge_panel_plugins.py", shell=True)
subprocess.call("purge_thunar_plugins.py", shell=True)
subprocess.call("purge_www.py", shell=True)
