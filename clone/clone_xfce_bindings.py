#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------ #
#
# Name: clone_xfce_bindings.py
# Purpose: Clone Xfce bindings repositories pulled from
#           https://gitlab.xfce.org/bindings
#
# version: 0.6
# updated: 20210213
# @author: kevin.bowen@gmail.com
#
# }}}} ------------------------------------------------------------------ #

import os
import sys
from modules import repo_arrays
from modules.repodir import repodir

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)


os.chdir(currentdir)
os.makedirs(repodir('bindings'), exist_ok=True)
os.chdir(repodir('bindings'))

for item in repo_arrays.xfce_bindings_list:
    os.system('git clone https://gitlab.xfce.org/bindings/' + item + '.git')
