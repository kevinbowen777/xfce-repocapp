#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------ #
#
# Name: pull_core.py
# Purpose: update local Xfce core repositories pulled from
#           https://gitlab.xfce.org/xfce
#
# version: 0.7.1
# updated: 20211207
# @author: kevin.bowen@gmail.com
#
# }}} ------------------------------------------------------------------ #

import cappdata

cappdata.pull_xfce(component='xfce', comp_list=cappdata.core_list())
