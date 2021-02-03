#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------- #
#
# Name: build_xfce_apps.py
# Purpose: Build local Xfce apps repositories
#
# version: 0.5
# updated: 20210203
# @author: kevin.bowen@gmail.com
#
# }}} ------------------------------------------------------------------- #

import os
import sys
import time
sys.path.append('./')

from repo_arrays import xfce_apps_list

os.chdir('../apps/')

os.environ["PKG_CONFIG_PATH"] = "/usr/lib/pkgconfig:/usr"

for item in xfce_apps_list:
    os.chdir(item)
    print('\nRunning autogen.sh for ' + item + '...\n')
    os.system('./autogen.sh --prefix=/usr')
    print('\nRunning make for ' + item + '...\n')
    time.sleep(1.5)
    os.system('make')
    os.chdir("..")
