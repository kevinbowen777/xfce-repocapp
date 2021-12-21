#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------ #
#
# Name: purge_core.py
# Purpose: delete the local Xfce4 core repositories originally pulled from
#           https://gitlab.xfce.org/xfce
#
# version: 0.7.1
# updated: 20211207
# @author: kevin.bowen@gmail.com
#
# }}} ------------------------------------------------------------------ #

import cappdata

cappdata.purge_xfce(component='xfce', comp_list=cappdata.core_list())
