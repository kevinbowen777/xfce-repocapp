#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------ #
#
# Name: purge_core.py
# Purpose: delete the local Xfce4 core repositories originally pulled from
#           https://gitlab.xfce.org/xfce
#
# version: 0.7
# updated: 20211207
# @author: kevin.bowen@gmail.com
#
# }}} ------------------------------------------------------------------ #

import os
import shutil
import cappdata

component = 'core'
success_count = 0

repopath = cappdata.repodir(component)
os.chdir(os.path.dirname(os.path.realpath(__file__)))

confirm = cappdata.query_yes_no(f"Are you sure you want to remove the "
                                f"Xfce '{component}' repositories? ")
if confirm == 'yes':
    for item in cappdata.core_list():
        filePath = (repopath + item)
        if os.path.isdir(repopath):
            try:
                shutil.rmtree(filePath)
                success_count += 1
                print('=' * 16)
                print(f"\nThe '{item}' directory has been deleted.\n")
                print(f"{success_count}/{len(cappdata.core_list())} "
                      f"'{component}' repositories deleted successfully.")
                print('=' * 16)
            except FileNotFoundError:
                print(f"The directory '{item}' does not exist. "
                      f"Skipping...")
                print('=' * 16)
    try:
        shutil.rmtree(repopath)
        print(f"\nThe directory '{component}' has been deleted.\n")
    except FileNotFoundError:
        print(f"The directory '{component}' does not exist. "
              f"Skipping...")
        print('=' * 16)
else:
    print("No repositories have been deleted. Have a nice day.")
