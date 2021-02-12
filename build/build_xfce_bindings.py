#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------- #
#
# Name: autogen_make_xfce_bindings.py
# Purpose: Build local Xfce bindings repositories
#
# version: 0.1
# updated: 20210130
# @author: kevin.bowen@gmail.com
#
# }}} ------------------------------------------------------------------- #

import os
import sys
import time
from repo_arrays import xfce_bindings_list

sys.path.append('./')


os.chdir('../bindings/')

os.environ["PKG_CONFIG_PATH"] = "/usr/lib/pkgconfig:/usr"

for item in xfce_bindings_list:
    os.chdir(item)
    print('\nRunning autogen.sh for ' + item + '...\n')
    os.system('./autogen.sh --prefix=/usr')
    print('\nRunning make for ' + item + '...\n')
    time.sleep(1.5)
    os.system('make')
    os.chdir("..")
