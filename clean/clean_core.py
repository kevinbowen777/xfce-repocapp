#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------- #
#
# Name: clean_core.py
# Purpose: Clean local Xfce core repository directories
#
# version: 0.7.1
# updated: 20211207
# @author: kevin.bowen@gmail.com
#
# }}} ------------------------------------------------------------------- #

import os
import time
import cappdata

component = 'core'
comp_list = cappdata.core_list()
repopath = cappdata.repodir(component)
success_count = 0

os.chdir(os.path.dirname(os.path.realpath(__file__)))

if os.path.isdir(repopath):
    os.chdir(repopath)
    for item in comp_list:
        if os.path.isdir(item):
            os.chdir(item)
            print('\nCleaning ' + item + ' directory...\n')
            time.sleep(1.5)
            os.system('make -s clean')
            success_count += 1
            print(f"{success_count}/{len(comp_list)} "
                  f"'{component}' repositories cleaned.")
            print('\nExiting ' + item + ' directory...\n')
            print('=' * 16)
            os.chdir('..')
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
