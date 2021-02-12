#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------ #
#
# Name: update_xfce_panel-plugins.py
# Purpose: update local Xfce panel-plugin repositories pulled from
#           https://gitlab.xfce.org/panel-plugins
#
# version: 0.5
# updated: 20210131
# @author: kevin.bowen@gmail.com
#
# }}} ------------------------------------------------------------------ #

import os
import sys
from repo_arrays import xfce_panel_plugins_list

sys.path.append('./')


os.chdir('../panel-plugins')

for item in xfce_panel_plugins_list:
    os.chdir(item)
    print('Updating ' + item + ':')
    os.system('git pull')
    os.chdir('../')
