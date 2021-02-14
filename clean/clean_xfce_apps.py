#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------- #
#
# Name: clean_xfce_apps.py
# Purpose: Clean local Xfce apps repository directories
#
# version: 0.2
# updated: 20210213
# @author: kevin.bowen@gmail.com
#
# }}} ------------------------------------------------------------------- #

import os
import sys
import time

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

import repo_arrays
from repodir import repodir

os.chdir(repodir('apps'))

for item in repo_arrays.xfce_apps_list:
    os.chdir(item)
    print('\nCleaning ' + item + ' directory...\n')
    time.sleep(1.5)
    os.system('make -s clean')
    print('\nExiting ' + item + ' directory...\n')
    os.chdir('..')
