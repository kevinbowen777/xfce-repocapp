#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------ #
#
# Name: install_apps.py
# Purpose: Install Xfce apps into system
#
# version: 0.7.1
# updated: 20211215
# @author: kevin.bowen@gmail.com
#
# }}} ------------------------------------------------------------------ #

import os
import cappdata

component = 'apps'
comp_list = cappdata.apps_list()
repopath = cappdata.repodir(component)

os.chdir(os.path.dirname(os.path.realpath(__file__)))

if os.path.isdir(repopath):
    os.chdir(repopath)
    for item in comp_list:
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
            print('\nNothing to do...\n')
            print(f"The '{item}' repo does not exist.\n\n"
                  "Perhaps you need to clone it first.\n")
            print('=' * 16)

else:
    print('Nothing to do...\n')
    print(f"The '{component}' repositories do not exist.\n\n"
          "Perhaps you need to clone the directory first.\n")
    print('=' * 16)
