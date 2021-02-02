#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------ #
#
# Name: update_xfce_apps.py
# Purpose: update local Xfce apps repositories pulled from
#           https://gitlab.xfce.org/apps
#
# version: 0.5
# updated: 20210131
# @author: kevin.bowen@gmail.com
#
# }}} ------------------------------------------------------------------ #

import os
import sys
sys.path.append('./')

from repo_arrays import xfce_apps_list

os.chdir('../apps')

for item in xfce_apps_list:
    os.chdir(item)
    print('Updating ' + item + ':')
    os.system('git pull')
    os.chdir('../')
