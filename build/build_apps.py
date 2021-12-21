#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------- #
#
# Name: build_apps.py
# Purpose: Build local Xfce apps repositories
#
# version: 0.7.1
# updated: 20211207
# @author: kevin.bowen@gmail.com
#
# }}} ------------------------------------------------------------------- #

import cappdata

cappdata.build_xfce(component='apps', comp_list=cappdata.apps_list())
