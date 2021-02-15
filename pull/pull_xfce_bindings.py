#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------ #
#
# Name: update_xfce_bindings.py
# Purpose: update local Xfce bindings repositories pulled from
#           https://gitlab.xfce.org/bindings
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
os.chdir(repodir('bindings'))

for item in repo_arrays.xfce_bindings_list:
    os.chdir(item)
    print('Updating ' + item + ':')
    os.system('git pull')
    os.chdir('../')
