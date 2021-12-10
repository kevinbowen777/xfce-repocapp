#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------ #
#
# Name: pull_bindings.py
# Purpose: update local Xfce bindings repositories pulled from
#           https://gitlab.xfce.org/bindings
#
# version: 0.7
# updated: 20211207
# @author: kevin.bowen@gmail.com
#
# }}} ------------------------------------------------------------------ #

import os
import cappdata

component = 'bindings'
success_count = 0

repopath = cappdata.repodir(component)
os.chdir(os.path.dirname(os.path.realpath(__file__)))

if os.path.isdir(repopath):
    os.chdir(cappdata.repodir(component))
    for item in cappdata.bindings_list():
        if os.path.isdir(item):
            os.chdir(item)
            print('Updating ' + item + ':')
            os.system('git pull')
            success_count += 1
            print(f"{success_count}/{len(cappdata.bindings_list())} "
                  f"'{component}' repositories updated successfully.")
            print('=' * 16)
            os.chdir('..')
        else:
            print(f"\nThe '{item}' repo does not exist. "
                  "Perhaps you need to clone it first.\n")
            print('=' * 16)
