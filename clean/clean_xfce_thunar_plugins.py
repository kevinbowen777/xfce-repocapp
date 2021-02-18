#!/usr/bin/env python3

# {{{ --------------------------------------------------------------------- #
#
# Name: clean_xfce_thunar_plugins.py
# Purpose: Clean local Xfce4 thunar-plugin repository directories
#
# version: 0.6
# updated: 20210218
# @author: kevin.bowen@gmail.com
#
# }}} --------------------------------------------------------------------- #

import os
import sys
import time

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from packages import repo_arrays
from packages.repodir import repodir

os.chdir(currentdir)
os.chdir(repodir('thunar-plugins'))

for item in repo_arrays.xfce_thunar_plugins_list:
    os.chdir(item)
    print('\nCleaning ' + item + ' directory...\n')
    time.sleep(1.5)
    os.system('make -s clean')
    print('\nExiting ' + item + ' directory...\n')
    print('========')
    os.chdir('..')
