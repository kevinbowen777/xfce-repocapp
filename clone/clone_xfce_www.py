#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------ #
#
# Name: clone_xfce_www.py
# Purpose: Clones Xfce4 www repositories pulled from
#           https://gitlab.xfce.org/www
#
# version: 0.5
# updated: 20210131
# @author: kevin.bowen@gmail.com
#
# }}} ------------------------------------------------------------------ #

import os
import sys
sys.path.append('./')
from repo_arrays import xfce_www_list


os.makedirs('../www', exist_ok=True)
os.chdir('../www')

for item in xfce_www_list:
    os.system('git clone https://gitlab.xfce.org/www/' + item + '.git')
