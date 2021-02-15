#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------ #
#
# Name: clone_xfce_thunar_plugins.py
# Purpose: Clones Xfce4 thunar-plugins repositories pulled from
#           https:/lab.xfce.org/thunar-plugins
#
# version: 0.6
# updated: 20210213
# @author: kevin.bowen@gmail.com
#
# }}} ------------------------------------------------------------------ #

import os
import sys
from modules import repo_arrays
from modules.repodir import repodir

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)


os.chdir(currentdir)
os.makedirs(repodir('thunar-plugins'), exist_ok=True)
os.chdir(repodir('thunar-plugins'))

for item in repo_arrays.xfce_thunar_plugins_list:
    os.system('git clone https://gitlab.xfce.org/thunar-plugins/'
              + item + '.git')
