#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------ #
#
# Name: clone_www.py
# Purpose: Clones Xfce4 www repositories pulled from
#           https://gitlab.xfce.org/www
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

component = 'www'

os.chdir(currentdir)
os.makedirs(cappdata.repodir('www'), exist_ok=True)
os.chdir(cappdata.repodir('www'))

clone_success_count = 0

for item in cappdata.www_list():
    if os.path.isdir('../' + component + '/' + item):
        print(f"\nThe '{item}' directory already exists. Skipping...\n")
        print('=' * 16)
    else:
        os.system('git clone https://gitlab.xfce.org/' + component + '/'
                  + item + '.git')
        clone_success_count += 1
        print('=' * 16)
        print(f"{clone_success_count}/{len(cappdata.www_list())} "
              f"'{component}' repositories cloned successfully.")
        print('=' * 16)
