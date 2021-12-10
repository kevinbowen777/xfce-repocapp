#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------ #
#
# Name: pull_apps.py
# Purpose: update local Xfce apps repositories pulled from
#           https://gitlab.xfce.org/apps
#
# version: 0.7
# updated: 20211207
# @author: kevin.bowen@gmail.com
#
# }}} ------------------------------------------------------------------ #

import os
import cappdata

component = 'apps'
success_count = 0

repopath = cappdata.repodir(component)
os.chdir(os.path.dirname(os.path.realpath(__file__)))

if os.path.isdir(repopath):
    os.chdir(cappdata.repodir(component))
    for item in cappdata.apps_list():
        if os.path.isdir(item):
            os.chdir(item)
            print('Updating ' + item + ':')
            os.system('git pull')
            success_count += 1
            print(f"{success_count}/{len(cappdata.apps_list())} "
                  f"'{component}' repositories updated successfully.")
            print('=' * 16)
            os.chdir('..')
        else:
            print(f"The '{item}' repo does not exist. "
                  "Perhaps you need to clone it first.\n")
            print('=' * 16)


