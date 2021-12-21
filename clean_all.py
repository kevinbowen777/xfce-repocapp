#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------ #
#
# Name: clean_all.py
# Purpose: clean oll of the Xfce repositories from
#           https://gitlab.xfce.org/
#
# version: 0.7.1
# updated: 20211207
# @author: kevin.bowen@gmail.com
#
# }}} ------------------------------------------------------------------ #

import cappdata

cappdata.clean_xfce(component='apps', comp_list=cappdata.apps_list())
cappdata.clean_xfce(component='bindings', comp_list=cappdata.bindings_list())
cappdata.clean_xfce(component='panel-plugins',
                    comp_list=cappdata.panel_plugins_list())
cappdata.clean_xfce(component='thunar-plugins',
                    comp_list=cappdata.thunar_plugins_list())
cappdata.clean_xfce(component='xfce', comp_list=cappdata.core_list())
