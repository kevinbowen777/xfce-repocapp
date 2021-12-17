#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------ #
#
# Name: pull_bindings.py
# Purpose: update local Xfce bindings repositories pulled from
#           https://gitlab.xfce.org/bindings
#
# version: 0.7.1
# updated: 20211207
# @author: kevin.bowen@gmail.com
#
# }}} ------------------------------------------------------------------ #

import os
import cappdata

component = 'bindings'
comp_list = cappdata.bindings_list()
repopath = cappdata.repodir(component)
success_count = 0

os.chdir(os.path.dirname(os.path.realpath(__file__)))

if os.path.isdir(repopath):
    os.chdir(repopath)
    for item in comp_list:
        if os.path.isdir(item):
            os.chdir(item)
            print('Updating ' + item + ':')
            os.system('git pull')
            success_count += 1
            print(f"\n{success_count}/{len(comp_list)} "
                  f"'{component}' repositories updated successfully.")
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
