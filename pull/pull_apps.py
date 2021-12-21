#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------ #
#
# Name: pull_apps.py
# Purpose: update local Xfce apps repositories pulled from
#           https://gitlab.xfce.org/apps
#
# version: 0.7.1
# updated: 20211207
# @author: kevin.bowen@gmail.com
#
# }}} ------------------------------------------------------------------ #

import cappdata

cappdata.pull_xfce(component='apps', comp_list=cappdata.apps_list())
