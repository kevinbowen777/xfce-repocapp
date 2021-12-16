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
import cappdata

component = 'www'
comp_list = cappdata.www_list()
repopath = cappdata.repodir(component)
success_count = 0

os.chdir(os.path.dirname(os.path.realpath(__file__)))
os.makedirs(repopath, exist_ok=True)
os.chdir(repopath)

for item in comp_list:
    if os.path.isdir(item):
        print(f"\nThe '{item}' directory already exists. Skipping...\n")
        print('=' * 16)
    else:
        os.system('git clone https://gitlab.xfce.org/' + component + '/'
                  + item + '.git')
        success_count += 1
        print('=' * 16)
        print(f"{item} repository cloned successfully")
        print(f"{success_count}/{len(comp_list)} "
              f"'{component}' repositories cloned successfully.")
        print('=' * 16)