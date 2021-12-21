#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------- #
#
# Name: autogen_make_xfce_panel_plugins.py
# Purpose: Build local Xfce panel-plugins repositories
#
# version: 0.7.1
# updated: 20211207
# @author: kevin.bowen@gmail.com
#
# }}} ------------------------------------------------------------------- #

import cappdata

cappdata.build_xfce(component='panel-plugins',
                    comp_list=cappdata.panel_plugins_list())
