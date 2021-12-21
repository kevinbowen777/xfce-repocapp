#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------ #
#
# Name: purge_www.py
# Purpose: delete the local Xfce www repositories pulled from
#           https://gitlab.xfce.org/www
#
# version: 0.7.1
# updated: 20211207
# @author: kevin.bowen@gmail.com
#
# }}} ------------------------------------------------------------------ #

import cappdata

cappdata.purge_xfce(component='www', comp_list=cappdata.www_list())
