#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------ #
#
# Name: clone_www.py
# Purpose: Clones Xfce4 www repositories pulled from
#           https://gitlab.xfce.org/www
#
# version: 0.7.1
# updated: 20211207
# @author: kevin.bowen@gmail.com
#
# }}} ------------------------------------------------------------------ #

import cappdata

cappdata.clone_xfce(component='www', comp_list=cappdata.www_list())
