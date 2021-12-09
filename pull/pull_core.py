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
import sys

import cappdata

component = 'core'

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

repopath = cappdata.repodir(component)
os.chdir(currentdir)

update_success_count = 0

if os.path.isdir(repopath):
    os.chdir(cappdata.repodir(component))
    for item in cappdata.core_list():
        if os.path.isdir('../' + component + '/' + item):
            os.chdir(item)
            print('Updating ' + item + ':')
            os.system('git pull')
            update_success_count += 1
            print(f"{update_success_count}/{len(cappdata.core_list())} "
                  f"'{component}' repositories updated successfully.")
            print('=' * 16)
            os.chdir('../')
        else:
            print(f"The '{item}' repo does not exist. "
                  "Perhaps you need to clone it first.\n")
            print('=' * 16)


