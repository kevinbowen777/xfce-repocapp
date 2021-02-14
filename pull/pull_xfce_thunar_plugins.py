#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------ #
#
# Name: update_xfce_thunar_plugins.py
# Purpose: update local Xfce thunar-plugin repositories pulled from
#           https://gitlab.xfce.org/thunar-plugins
#
# version: 0.6
# updated: 20210213
# @author: kevin.bowen@gmail.com
#
# }}} ------------------------------------------------------------------ #

import os
import sys
import repo_arrays
from repodir import repodir

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)


os.chdir(currentdir)
os.chdir(repodir('thunar-plugins'))

for item in repo_arrays.xfce_thunar_plugins_list:
    os.chdir(item)
    print('Updating ' + item + ':')
    os.system('git pull')
    os.chdir('../')
