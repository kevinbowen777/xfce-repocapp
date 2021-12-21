#!/usr/bin/env python3

# {{{ --------------------------------------------------------------------- #
#
# Name: clean_thunar_plugins.py
# Purpose: Clean local Xfce4 thunar-plugin repository directories
#
# version: 0.7.1
# updated: 20211207
# @author: kevin.bowen@gmail.com
#
# }}} --------------------------------------------------------------------- #

import cappdata

cappdata.clean_xfce(component='thunar-plugins',
                    comp_list=cappdata.thunar_plugins_list())
