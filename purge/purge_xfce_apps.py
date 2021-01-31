#!/usr/bin/env python3

# ---------------------------------------------------------------------- #
#
# Name: purge_xfce_apps.py
# Purpose: delete the local Xfce apps repositories originally pulled from
#           https://gitlab.xfce.org/apps
#
# version: 0.5
# updated: 20210131
# @author: kevin.bowen@gmail.com
#
# ---------------------------------------------------------------------- #

import os
import sys
sys.path.append('./')

from repo_arrays import xfce_apps_list

confirm = input('Are you sure you want to remove the Xfce app repos[y|n]? ')
if confirm.lower() == 'y':
    for item in xfce_apps_list:
        os.system('rm -rf ../apps/' + item)
        print("The " + item + " Xfce app repo has been purged.")
    os.system('rmdir ../apps/')
    print('The apps directory has been deleted.')
else:
    print("No repositories have been deleted. Have a nice day.")
