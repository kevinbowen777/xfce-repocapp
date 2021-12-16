#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------- #
#
# Name: autogen_make_xfce_panel_plugins.py
# Purpose: Build local Xfce panel-plugins repositories
#
# version: 0.7
# updated: 20211207
# @author: kevin.bowen@gmail.com
#
# }}} ------------------------------------------------------------------- #

import os
import time
import cappdata

component = 'panel-plugins'
comp_list = cappdata.panel_plugins_list()
repopath = cappdata.repodir(component)
os.environ["PKG_CONFIG_PATH"] = "/usr/lib/pkgconfig:/usr"

os.chdir(os.path.dirname(os.path.realpath(__file__)))

if os.path.isdir(repopath):
    os.chdir(repopath)
    for item in comp_list:
        if os.path.isdir(item):
            os.chdir(item)
            print('\nRunning autogen.sh for ' + item + '...\n')
            os.system('./autogen.sh --prefix=/usr')
            print('\nRunning make for ' + item + '...\n')
            time.sleep(1.5)
            os.system('make')
            print('=' * 16)
            os.chdir("..")
        else:
            print('\nNothing to do...\n')
            print(f"The '{item}' repo does not exist.\n\n"
                  "Perhaps you need to clone it first.\n")
            print('=' * 16)

else:
    print('Nothing to do...\n')
    print(f"The '{component}' repositories do not exist.\n\n"
          "Perhaps you need to clone the directory first.\n")
    print('=' * 16)
