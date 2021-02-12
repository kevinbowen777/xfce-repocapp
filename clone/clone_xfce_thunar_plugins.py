#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------ #
#
# Name: clone_xfce_thunar_plugins.py
# Purpose: Clones Xfce4 thunar-plugins repositories pulled from
#           https:/lab.xfce.org/thunar-plugins
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


os.makedirs('../thunar-plugins', exist_ok=True)
os.chdir('../thunar-plugins')

for item in xfce_thunar_plugins_list:
    os.system('git clone https://gitlab.xfce.org/thunar-plugins/' + item + '.git')
