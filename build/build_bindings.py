#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------- #
#
# Name: build_bindings.py
# Purpose: Build local Xfce bindings repositories
#
# version: 0.7
# updated: 20211207
# @author: kevin.bowen@gmail.com
#
# }}} ------------------------------------------------------------------- #

import os
import time
import cappdata

component = 'bindings'

os.chdir(os.path.dirname(os.path.realpath(__file__)))
os.environ["PKG_CONFIG_PATH"] = "/usr/lib/pkgconfig:/usr"

for item in cappdata.bindings_list():
    os.chdir((cappdata.repodir(component)) + item)
    print(os.path.dirname(os.path.realpath(__file__)))
    print('\nRunning autogen.sh for ' + item + '...\n')
    os.system('./autogen.sh --prefix=/usr')
    print('\nRunning make for ' + item + '...\n')
    time.sleep(1.5)
    os.system('make')
