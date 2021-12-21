#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------ #
#
# Name: purge_bindings.py
# Purpose: delete the local Xfce bindings repositories originally pulled from
#           https://gitlab.xfce.org/bindings
#
# version: 0.7.1
# updated: 20211207
# @author: kevin.bowen@gmail.com
#
# }}} ------------------------------------------------------------------ #

import cappdata

cappdata.purge_xfce(component='bindings', comp_list=cappdata.bindings_list())
