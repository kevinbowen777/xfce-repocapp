#!/usr/bin/env python3

# ---------------------------------------------------------------------- #
#
# Name: update_xfce_www.py
# Purpose: update local Xfce www repositories pulled from
#           https://gitlab.xfce.org/www
#
# version: 0.5
# updated: 20210131
# @author: kevin.bowen@gmail.com
#
# ---------------------------------------------------------------------- #

import os
import sys
sys.path.append('./')

from repo_arrays import xfce_www_list

os.chdir('../www')

for item in xfce_www_list:
    os.chdir(item)
    print('Updating ' + item + ':')
    os.system('git pull')
    os.chdir('../')
