#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------- #
#
# Name: build_bindings.py
# Purpose: Build local Xfce bindings repositories
#
# version: 0.7.1
# updated: 20211207
# @author: kevin.bowen@gmail.com
#
# }}} ------------------------------------------------------------------- #

import cappdata

cappdata.build_xfce(component='bindings', comp_list=cappdata.bindings_list())
