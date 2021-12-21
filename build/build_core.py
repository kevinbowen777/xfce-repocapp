#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------- #
#
# Name: build_core.py
# Purpose: Build local Xfce core repositories
#
# version: 0.7.1
# updated: 20211207
# @author: kevin.bowen@gmail.com
#
# }}} ------------------------------------------------------------------- #

import cappdata

cappdata.build_xfce(component='xfce', comp_list=cappdata.core_list())
