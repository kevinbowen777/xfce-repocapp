#!/usr/bin/env python3

# ---------------------------------------------------------------------- #
#
# Name: purge_xfce_core.py
# Purpose: delete the local Xfce4 core repositories originally pulled from
#           https://gitlab.xfce.org/xfce
#
# version: 0.5
# updated: 20210131
# @author: kevin.bowen@gmail.com
#
# ---------------------------------------------------------------------- #

import os
import sys
sys.path.append('./')

from repo_arrays import xfce_core_list

confirm = input('Are you sure you want to remove the Xfce core repos[y|n]? ')
if confirm.lower() == 'y':
    for item in xfce_core_list:
        os.system('rm -rf ../core/' + item)
        print("The " + item + " Xfce core repo has been purged.")
    os.system('rmdir ../core/')
    print('The core directory has been deleted.')
else:
    print("No repositories have been deleted. Have a nice day.")
