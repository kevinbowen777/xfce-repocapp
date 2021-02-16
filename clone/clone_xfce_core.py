#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------ #
#
# Name: clone_xfce_core.py
# Purpose: Clones Xfce core repositories pulled from
#           https://gitlab.xfce.org/xfce
#
# version: 0.6
# updated: 20210213
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
os.makedirs(repodir('core'), exist_ok=True)
os.chdir(repodir('core'))

for item in repo_arrays.xfce_core_list:
    os.system('git clone https://gitlab.xfce.org/xfce/' + item + '.git')
