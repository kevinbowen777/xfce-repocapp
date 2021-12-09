#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------ #
#
# Name: clone_core.py
# Purpose: Clones Xfce core repositories pulled from
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

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

component = 'core'

os.chdir(currentdir)
os.makedirs(cappdata.repodir('core'), exist_ok=True)
os.chdir(cappdata.repodir('core'))

clone_success_count = 0

for item in cappdata.core_list():
    if os.path.isdir('../' + component + '/' + item):
        print(f"\nThe '{item}' directory already exists. Skipping...\n")
        print('=' * 16)
    else:
        # Public name of this repo is called Xfce, not 'core'.
        os.system('git clone https://gitlab.xfce.org/xfce/'
                  + item + '.git')
        clone_success_count += 1
        print('=' * 16)
        print(f"{clone_success_count}/{len(cappdata.core_list())} "
              f"'{component}' repositories cloned successfully.")
        print('=' * 16)
