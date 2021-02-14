#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------ #
#
# Name: purge_xfce_panel_plugins.py
# Purpose: delete the local Xfce panel-plugins repositories pulled from
#           https://gitlab.xfce.org/panel-plugins
#
# version: 0.6
# updated: 20210212
# @author: kevin.bowen@gmail.com
#
# }}} ------------------------------------------------------------------ #

import os
import sys
import shutil
from repo_arrays import xfce_panel_plugins_list
from query import query_yes_no
from repodir import repodir

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)


repopath = repodir('panel-plugins')
os.chdir(currentdir)

confirm = query_yes_no('Are you sure you want to remove the Xfce '
                       'panel-plugins repositories? ')
if confirm == 'yes':
    for item in xfce_panel_plugins_list:
        filePath = (repopath + item)
        try:
            shutil.rmtree(filePath)
            print(item + ' directory has been deleted.')
        except ValueError:
            print("Error while deleting", item + " directory.")
    try:
        shutil.rmtree(repopath)
        print('The panel-plugins directory has been deleted.')
    except ValueError:
        print("Error while deleting panel-plugins directory.")
else:
    print("No repositories have been deleted. Have a nice day.")
