#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------ #
#
# Name: install_panel_plugins.py
# Purpose: Install Xfce4 panel-plugins into system
#
# version: 0.7
# updated: 20211207
# @author: kevin.bowen@gmail.com
#
# }}} ------------------------------------------------------------------ #

import os
import cappdata

component = 'panel-plugins'

repopath = cappdata.repodir(component)
os.chdir(os.path.dirname(os.path.realpath(__file__)))

if os.path.isdir(repopath):
    os.chdir(cappdata.repodir(component))
    for item in cappdata.panel_plugins_list():
        if os.path.isdir(item):
            os.chdir(item)
            confirm = cappdata.query_yes_no(
                f"Do you want to install '{item}' to the system? "
                f"Answer 'No' to install locally. ")
            if confirm == 'yes':
                print('Installing ' + item + ' to the system...')
                os.system('sudo make install')
                print('=' * 16)
                os.chdir("..")
            else:
                print('Installing ' + item + ' locally...')
                os.system('make install')
                print('=' * 16)
                os.chdir("..")
        else:
            print(f"\nThe '{item}' repo does not exist. "
                  "Perhaps you need to clone & build it first.\n")
            print('=' * 16)
