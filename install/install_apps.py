#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------ #
#
# Name: install_apps.py
# Purpose: Install Xfce apps into system
#
# version: 0.7.1
# updated: 20211215
# @author: kevin.bowen@gmail.com
#
# }}} ------------------------------------------------------------------ #

import cappdata

cappdata.install_xfce(component='apps', comp_list=cappdata.apps_list())
