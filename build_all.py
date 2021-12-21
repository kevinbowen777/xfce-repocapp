#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------ #
#
# Name: build_all.py
# Purpose: build oll of the Xfce repositories from
#           https://gitlab.xfce.org/
#
# version: 0.7.1
# updated: 20211207
# @author: kevin.bowen@gmail.com
#
# }}} ------------------------------------------------------------------ #

import cappdata

cappdata.build_xfce(component='apps', comp_list=cappdata.apps_list())
cappdata.build_xfce(component='bindings', comp_list=cappdata.bindings_list())
cappdata.build_xfce(component='panel-plugins',
                    comp_list=cappdata.panel_plugins_list())
cappdata.build_xfce(component='thunar-plugins',
                    comp_list=cappdata.thunar_plugins_list())
cappdata.build_xfce(component='xfce', comp_list=cappdata.core_list())
