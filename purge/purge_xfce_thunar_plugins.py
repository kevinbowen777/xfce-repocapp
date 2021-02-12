#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------ #
#
# Name: purge_xfce_thunar_plugins.py
# Purpose: delete the local Xfce thunar-plugin repositories pulled from
#           https://gitlab.xfce.org/thunar-plugins
#
# version: 0.5
# updated: 20210131
# @author: kevin.bowen@gmail.com
#
# }}} ------------------------------------------------------------------ #

import os
import sys
sys.path.append('./')
from repo_arrays import xfce_thunar_plugins_list


confirm = input('Are you sure you want to remove the Xfce thunar-plugins'
                ' repositories[y|n]? ')
if confirm.lower() == 'y':
    for item in xfce_thunar_plugins_list:
        os.system('rm -rf ../thunar-plugins/' + item)
        print("The " + item + " Xfce thunar-plugin repo has been purged.")
    os.system('rmdir ../thunar-plugins/')
    print('The thunar-plugins directory has been deleted.')
else:
    print("No repositories have been deleted. Have a nice day.")
