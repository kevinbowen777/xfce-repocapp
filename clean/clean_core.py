#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------- #
#
# Name: clean_core.py
# Purpose: Clean local Xfce core repository directories
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
success_count = 0

repopath = cappdata.repodir(component)
os.chdir(os.path.dirname(os.path.realpath(__file__)))

if os.path.isdir(repopath):
    os.chdir(cappdata.repodir(component))
    for item in cappdata.core_list():
        if os.path.isdir(item):
            os.chdir(item)
            print('\nCleaning ' + item + ' directory...\n')
            time.sleep(1.5)
            os.system('make -s clean')
            success_count += 1
            print(f"{success_count}/{len(cappdata.core_list())} "
                  f"'{component}' repositories cleaned.")
            print('\nExiting ' + item + ' directory...\n')
            print('=' * 16)
            os.chdir('..')
        else:
            print(f"\nThe '{item}' repo does not exist. "
                  "Perhaps you need to clone & build it first.\n")
            print('=' * 16)
