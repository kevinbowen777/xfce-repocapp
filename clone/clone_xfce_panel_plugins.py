#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------ #
#
# Name: clone_xfce_panel_plugins.py
# Purpose: Clones Xfce4 panel-plugins repositories pulled  from
#           https://gitlab.xfce.org/panel-plugins
#
# version: 0.6
# updated: 20210218
# @author: kevin.bowen@gmail.com
#
# }}} ------------------------------------------------------------------ #

import os
import sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from packages import repo_arrays
from packages.repodir import repodir

os.chdir(currentdir)
os.makedirs(repodir('panel-plugins'), exist_ok=True)
os.chdir(repodir('panel-plugins'))

for item in repo_arrays.xfce_panel_plugins_list:
    os.system('git clone https://gitlab.xfce.org/panel-plugins/'
              + item + '.git')
    print('========')
