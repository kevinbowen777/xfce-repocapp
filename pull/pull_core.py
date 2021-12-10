#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------ #
#
# Name: pull_core.py
# Purpose: update local Xfce core repositories pulled from
#           https://gitlab.xfce.org/xfce
#
# version: 0.7
# updated: 20211207
# @author: kevin.bowen@gmail.com
#
# }}} ------------------------------------------------------------------ #

import os
import cappdata

component = 'core'
success_count = 0

repopath = cappdata.repodir(component)
os.chdir(os.path.dirname(os.path.realpath(__file__)))

if os.path.isdir(repopath):
    os.chdir(cappdata.repodir(component))
    for item in cappdata.core_list():
        if os.path.isdir():
            os.chdir(item)
            print('Updating ' + item + ':')
            os.system('git pull')
            success_count += 1
            print(f"{success_count}/{len(cappdata.core_list())} "
                  f"'{component}' repositories updated successfully.")
            print('=' * 16)
            os.chdir('..')
        else:
            print(f"The '{item}' repo does not exist. "
                  "Perhaps you need to clone it first.\n")
            print('=' * 16)


