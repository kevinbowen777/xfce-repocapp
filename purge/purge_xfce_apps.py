#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------ #
#
# Name: purge_xfce_apps.py
# Purpose: delete the local Xfce apps repositories originally pulled from
#           https://gitlab.xfce.org/apps
#
# version: 0.6
# updated: 20210218
# @author: kevin.bowen@gmail.com
#
# }}} ------------------------------------------------------------------ #

import os
import shutil
import sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from packages.repo_arrays import xfce_apps_list
from packages.query import query_yes_no
from packages.repodir import repodir


repopath = repodir('apps')
os.chdir(currentdir)

confirm = query_yes_no('This will remove the Xfce apps repositories. ')
if confirm == 'yes':
    for item in xfce_apps_list:
        filePath = (repopath + item)
        try:
            shutil.rmtree(filePath)
            print(item + ' directory has been deleted.')
        except ValueError:
            print("Error while deleting", item + " directory.")
    try:
        shutil.rmtree(repopath)
        print('The apps directory has been deleted.')
    except ValueError:
        print("Error while deleting apps directory.")
else:
    print("No repositories have been deleted. Have a nice day.")
