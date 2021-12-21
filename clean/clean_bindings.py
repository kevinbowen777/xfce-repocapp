#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------- #
#
# Name: clean_bindings.py
# Purpose: Clean local Xfce bindings repository directories
#
# version: 0.7.1
# updated: 20211207
# @author: kevin.bowen@gmail.com
#
# }}} ------------------------------------------------------------------- #

import cappdata

cappdata.clean_xfce(component='bindings', comp_list=cappdata.bindings_list())
