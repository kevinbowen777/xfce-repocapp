#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------- #
#
# Name: build_xfce_core.py
# Purpose: Build local Xfce core repositories
#
# version: 0.6
# updated: 20210213
# @author: kevin.bowen@gmail.com
#
# }}} ------------------------------------------------------------------- #

import os
import sys
import time
from modules import repo_arrays
from modules.repodir import repodir

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)


os.chdir(currentdir)
os.chdir(repodir('core'))
os.environ["PKG_CONFIG_PATH"] = "/usr/lib/pkgconfig:/usr"

for item in repo_arrays.xfce_core_list:
    os.chdir(item)
    print('\nRunning autogen.sh for ' + item + '...\n')
    os.system('./autogen.sh --prefix=/usr')
    print('\nRunning make for ' + item + '...\n')
    time.sleep(1.5)
    os.system('make')
    os.chdir("..")
