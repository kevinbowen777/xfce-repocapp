#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------- #
#
# Name: clean_apps.py
# Purpose: Clean local Xfce apps repository directories
#
# version: 0.7.1
# updated: 20211207
# @author: kevin.bowen@gmail.com
#
# }}} ------------------------------------------------------------------- #

import cappdata

cappdata.clean_xfce(component='apps', comp_list=cappdata.apps_list())
