#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------ #
#
# Name: pull_xfce_apps.py
# Purpose: update local Xfce apps repositories pulled from
#           https://gitlab.xfce.org/apps
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
    print('Updating ' + item + ':')
    os.system('git pull')
    print('========')
    os.chdir('../')
