#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------ #
#
# Name: purge_xfce_core.py
# Purpose: delete the local Xfce4 core repositories originally pulled from
#           https://gitlab.xfce.org/xfce
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

from repo_arrays import xfce_core_list
from query import query_yes_no
from repodir import repodir

repopath = repodir('core')
os.chdir(currentdir)

confirm = query_yes_no('Are you sure you want to remove the Xfce core '
                       'repositories? ')
if confirm == 'yes':
    for item in xfce_core_list:
        filePath = (repopath + item)
        try:
            shutil.rmtree(filePath)
            print(item + ' directory has been deleted.')
        except ValueError:
            print("Error while deleting", item + " directory.")
    try:
        shutil.rmtree(repopath)
        print('The core directory has been deleted.')
    except ValueError:
        print("Error while deleting core directory.")
else:
    print("No repositories have been deleted. Have a nice day.")
