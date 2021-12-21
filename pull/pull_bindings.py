#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------ #
#
# Name: pull_bindings.py
# Purpose: update local Xfce bindings repositories pulled from
#           https://gitlab.xfce.org/bindings
#
# version: 0.7.1
# updated: 20211207
# @author: kevin.bowen@gmail.com
#
# }}} ------------------------------------------------------------------ #

import cappdata

cappdata.pull_xfce(component='bindings', comp_list=cappdata.bindings_list())
