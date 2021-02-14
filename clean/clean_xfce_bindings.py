#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------- #
#
# Name: clean_xfce_bindings.py
# Purpose: Clean local Xfce bindings repository directories
#
# version: 0.2
# updated: 20210213
# @author: kevin.bowen@gmail.com
#
# }}} ------------------------------------------------------------------- #

import os
import sys
import time
import repo_arrays
from repodir import repodir

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)


os.chdir(currentdir)
os.chdir(repodir('bindings'))

for item in repo_arrays.xfce_bindings_list:
    os.chdir(item)
    print('\nCleaning ' + item + ' directory...\n')
    time.sleep(1.5)
    os.system('make -s clean')
    print('\nExiting ' + item + ' directory...\n')
    os.chdir('..')
