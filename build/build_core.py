#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------- #
#
# Name: build_core.py
# Purpose: Build local Xfce core repositories
#
# version: 0.7
# updated: 20211207
# @author: kevin.bowen@gmail.com
#
# }}} ------------------------------------------------------------------- #

import os
import time

import cappdata

component = 'core'

os.chdir(os.path.dirname(os.path.realpath(__file__)))
os.chdir(cappdata.repodir(component))
os.environ["PKG_CONFIG_PATH"] = "/usr/lib/pkgconfig:/usr"

for item in cappdata.core_list():
    os.chdir(item)
    print('\nRunning autogen.sh for ' + item + '...\n')
    os.system('./autogen.sh --prefix=/usr')
    print('\nRunning make for ' + item + '...\n')
    time.sleep(1.5)
    os.system('make')
    os.chdir("..")
