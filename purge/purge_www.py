#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------ #
#
# Name: purge_www.py
# Purpose: delete the local Xfce www repositories pulled from
#           https://gitlab.xfce.org/www
#
# version: 0.7.1
# updated: 20211207
# @author: kevin.bowen@gmail.com
#
# }}} ------------------------------------------------------------------ #

import os
import shutil
import cappdata

component = 'www'
comp_list = cappdata.www_list()
success_count = 0
repopath = cappdata.get_path(component)

os.chdir(os.path.dirname(os.path.realpath(__file__)))
confirm = cappdata.query_yes_no(f"Are you sure you want to remove the "
                                f"Xfce '{component}' repositories? ")

if confirm == 'yes':
    if os.path.isdir(repopath):
        os.chdir(repopath)
        for item in comp_list:
            filePath = (repopath + item)
            if os.path.isdir(item):
                try:
                    shutil.rmtree(item)
                    success_count += 1
                    print(f"\nThe '{item}' directory has been deleted.\n")
                    print(f"{success_count}/{len(comp_list)} "
                          f"'{component}' repositories deleted successfully.")
                    print('=' * 16)
                except FileNotFoundError:
                    print(f"The directory '{item}' does not exist. "
                          f"Skipping...")
                    print('=' * 16)
        os.chdir('..')
        shutil.rmtree(component)
        print(f"\nThe directory '{component}' has been deleted.\n")
        print('=' * 16)
    else:
        print('Nothing to do...\n')
        print(f"The '{component}' repositories do not exist.\n\n"
              "Perhaps you need to clone the directory first.\n")
        print('=' * 16)

else:
    print("No repositories have been deleted. Have a nice day.")
