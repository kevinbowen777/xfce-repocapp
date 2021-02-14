#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------ #
#
# Name: install_xfce_core.py
# Purpose: install local Xfce core repositories
#
# version: 0.2
# updated: 20210213
# @author: kevin.bowen@gmail.com
#
# }}} ------------------------------------------------------------------ #

import os
import sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

import repo_arrays
from repodir import repodir

os.chdir(repodir('core'))

for item in repo_arrays.xfce_core_list:
    os.chdir(item)
    os.system('sudo make install')
    os.chdir("..")
