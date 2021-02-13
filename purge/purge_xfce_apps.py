#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------ #
#
# Name: purge_xfce_apps.py
# Purpose: delete the local Xfce apps repositories originally pulled from
#           https://gitlab.xfce.org/apps
#
# version: 0.6
# updated: 20210212
# @author: kevin.bowen@gmail.com
#
# }}} ------------------------------------------------------------------ #

import os
import sys
import shutil

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from repo_arrays import xfce_apps_list
from query import query_yes_no

os.chdir(currentdir)

confirm = query_yes_no('Are you sure you want to remove the Xfce apps repositories? ')
if confirm == 'yes':
    for item in xfce_apps_list:
        filePath = ('../../apps/' + item)
        try:
            shutil.rmtree(filePath)
            print(item + ' directory has been deleted.')
        except:
            print("Error while deleting", item + " directory.")
    try:
        shutil.rmtree('../../apps')
        print('The apps directory has been deleted.')
    except:
        print("Error while deleting apps directory.")
else:
    print("No repositories have been deleted. Have a nice day.")
