#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------- #
#
# Name: autogen_make_xfce_panel_plugins.py
# Purpose: Build local Xfce panel-plugins repositories
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

from repo_arrays import xfce_panel_plugins_list

os.chdir('../panel-plugins/')

os.environ["PKG_CONFIG_PATH"] = "/usr/lib/pkgconfig:/usr"

for item in xfce_panel_plugins_list:
    os.chdir(item)
    print('\nRunning autogen.sh for ' + item + '...\n')
    os.system('./autogen.sh --prefix=/usr')
    print('\nRunning make for ' + item + '...\n')
    time.sleep(1.5)
    os.system('make')
    os.chdir("..")
