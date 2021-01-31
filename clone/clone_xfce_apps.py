#!/usr/bin/env python3

# ---------------------------------------------------------------------- #
#
# Name: clone_xfce_apps.py
# Purpose: Clones Xfce apps repositories pulled from
#           https://gitlab.xfce.org/apps
#
# version: 0.5
# updated: 20210131
# @author: kevin.bowen@gmail.com
#
# ---------------------------------------------------------------------- #

import os
import sys
sys.path.append('./')

from repo_arrays import xfce_apps_list

os.makedirs('../apps', exist_ok=True)
os.chdir('../apps')

for item in xfce_apps_list:
    os.system('git clone https://gitlab.xfce.org/apps/' + item + '.git')
