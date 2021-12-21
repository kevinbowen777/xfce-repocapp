#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------- #
#
# Name: clean_core.py
# Purpose: Clean local Xfce core repository directories
#
# version: 0.7.1
# updated: 20211207
# @author: kevin.bowen@gmail.com
#
# }}} ------------------------------------------------------------------- #

import cappdata

cappdata.clean_xfce(component='xfce', comp_list=cappdata.core_list())
