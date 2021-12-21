#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------ #
#
# Name: purge_apps.py
# Purpose: delete the local Xfce apps repositories originally pulled from
#           https://gitlab.xfce.org/apps
#
# version: 0.7.1
# updated: 20211207
# @author: kevin.bowen@gmail.com
#
# }}} ------------------------------------------------------------------ #

import cappdata

cappdata.purge_xfce(component='apps', comp_list=cappdata.apps_list())
