#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------ #
#
# Name: purge_xfce_panel_plugins.py
# Purpose: delete the local Xfce panel-plugins repositories pulled from
#           https://gitlab.xfce.org/panel-plugins
#
# version: 0.5
# updated: 20210131
# @author: kevin.bowen@gmail.com
#
# }}} ------------------------------------------------------------------ #

import os
import sys
sys.path.append('./')

from repo_arrays import xfce_panel_plugins_list

confirm = input('Are you sure you want to remove the Xfce panel-plugins'
                ' repositories[y|n]? ')
if confirm.lower() == 'y':
    for item in xfce_panel_plugins_list:
        os.system('rm -rf ../panel-plugins/' + item)
        print("The " + item + " Xfce panel-plugin repo has been purged.")
    os.system('rmdir ../panel-plugins/')
    print('The panel-plugins directory has been deleted.')
else:
    print("No repositories have been deleted. Have a nice day.")
