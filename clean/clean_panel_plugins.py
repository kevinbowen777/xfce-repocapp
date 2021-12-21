#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------- #
#
# Name: clean_panel_plugins.py
# Purpose: Clean local Xfce panel-plugins repository directories
#
# version: 0.7.1
# updated: 20211207
# @author: kevin.bowen@gmail.com
#
# }}} ------------------------------------------------------------------- #

import cappdata

cappdata.clean_xfce(component='panel-plugins',
                    comp_list=cappdata.panel_plugins_list())
