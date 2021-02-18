#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------ #
#
# Name: install_xfce_apps.py
# Purpose: Install Xfce apps into system
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
os.chdir(repodir('apps'))

for item in repo_arrays.xfce_apps_list:
    os.chdir(item)
    print('Installing ' + item + '...')
    os.system('sudo make install')
    print('========')
    os.chdir("..")
