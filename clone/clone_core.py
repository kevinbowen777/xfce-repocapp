#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------ #
#
# Name: clone_core.py
# Purpose: Clones Xfce core repositories pulled from
#           https://gitlab.xfce.org/xfce
#
# version: 0.7.1
# updated: 20211207
# @author: kevin.bowen@gmail.com
#
# }}} ------------------------------------------------------------------ #

import cappdata

cappdata.clone_xfce(component='xfce', comp_list=cappdata.core_list())
