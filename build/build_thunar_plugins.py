#!/usr/bin/env python3

# {{{ --------------------------------------------------------------------- #
#
# Name: build_thunar_plugins.py
# Purpose: Build local Xfce4 thunar-plugins repositories
#
# version: 0.7.1
# updated: 20211207
# @author: kevin.bowen@gmail.com
#
# }}} --------------------------------------------------------------------- #

import cappdata

cappdata.build_xfce(component='thunar-plugins',
                    comp_list=cappdata.thunar_plugins_list())
