#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------ #
#
# Name: purge_xfce_all.py
# Purpose: delete oll of the local Xfce repositories pulled from
#           https://gitlab.xfce.org/
#
# version: 0.1
# updated: 20210215
# @author: kevin.bowen@gmail.com
#
# }}} ------------------------------------------------------------------ #


import os
import subprocess
import sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
os.chdir(currentdir)


subprocess.call("purge_xfce_apps.py", shell=True)
subprocess.call("purge_xfce_bindings.py", shell=True)
subprocess.call("purge_xfce_core.py", shell=True)
subprocess.call("purge_xfce_panel_plugins.py", shell=True)
subprocess.call("purge_xfce_thunar_plugins.py", shell=True)
subprocess.call("purge_xfce_www.py", shell=True)
