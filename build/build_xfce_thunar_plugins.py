#!/usr/bin/env python3

# {{{ --------------------------------------------------------------------- #
#
# Name: build_make_xfce_thunar_plugins.py
# Purpose: Build local Xfce4 thunar-plugins repositories
#
# version: 0.5
# updated: 20210203
# @author: kevin.bowen@gmail.com
#
# }}} --------------------------------------------------------------------- #

import os
import sys
import time
from repo_arrays import xfce_thunar_plugins_list

sys.path.append('./')


os.chdir('../thunar-plugins/')

os.environ["PKG_CONFIG_PATH"] = "/usr/lib/pkgconfig:/usr"

for item in xfce_thunar_plugins_list:
    os.chdir(item)
    print('\nRunning autogen.sh for ' + item + '...\n')
    os.system('./autogen.sh --prefix=/usr')
    print('\nRunning make for ' + item + '...\n')
    time.sleep(1.5)
    os.system('make')
    os.chdir("..")
