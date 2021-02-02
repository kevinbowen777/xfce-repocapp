#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------ #
#
# Name: clone_xfce_panel_plugins.py
# Purpose: Clones Xfce4 panel-plugins repositories pulled  from
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

os.makedirs('../panel-plugins', exist_ok=True)
os.chdir('../panel-plugins')

for item in xfce_panel_plugins_list:
    os.system('git clone https://gitlab.xfce.org/panel-plugins/' + item + '.git')
