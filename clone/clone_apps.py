#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------ #
#
# Name: clone_apps.py
# Purpose: Clones Xfce apps repositories pulled from
#           https://gitlab.xfce.org/apps
#
# version: 0.7.1
# updated: 20211207
# @author: kevin.bowen@gmail.com
#
# }}} ------------------------------------------------------------------ #

import cappdata

cappdata.clone_xfce(component='apps', comp_list=cappdata.apps_list())
