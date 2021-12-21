#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------ #
#
# Name: purge_panel_plugins.py
# Purpose: delete the local Xfce panel-plugins repositories pulled from
#           https://gitlab.xfce.org/panel-plugins
#
# version: 0.7.1
# updated: 20211207
# @author: kevin.bowen@gmail.com
#
# }}} ------------------------------------------------------------------ #

import cappdata

cappdata.purge_xfce(component='panel-plugins',
                    comp_list=cappdata.panel_plugins_list())
