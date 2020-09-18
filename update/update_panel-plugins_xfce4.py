#!/usr/bin/env python3

# ---------------------------------------------------------------------- #
#
# Name: update_panel_plugins_xfce4.py
# Purpose: Updates Xfce4 git panel-plugins repos from
#             gitlab.xfce.org/panel-plugins
#
# version: 0.1
# updated: 20200917
# @author: kevin.bowen@gmail.com
#
# ---------------------------------------------------------------------- #

import os


panel_list = ['xfce4-battery-plugin', 'xfce4-calculator-plugin',
              'xfce4-clipman-plugin', 'xfce4-cpufreq-plugin',
              'xfce4-cpugraph-plugin', 'xfce4-datetime-plugin',
              'xfce4-diskperf-plugin', 'xfce4-embed-plugin',
              'xfce4-eyes-plugin', 'xfce4-fsguard-plugin',
              'xfce4-genmon-plugin', 'xfce4-indicator-plugin',
              'xfce4-mailwatch-plugin', 'xfce4-mount-plugin',
              'xfce4-mpc-plugin', 'xfce4-netload-plugin',
              'xfce4-notes-plugin', 'xfce4-places-plugin',
              'xfce4-pulseaudio-plugin', 'xfce4-sample-plugin',
              'xfce4-sensors-plugin', 'xfce4-smartbookmark-plugin',
              'xfce4-statusnotifier-plugin', 'xfce4-stopwatch-plugin',
              'xfce4-systemload-plugin', 'xfce4-time-out-plugin',
              'xfce4-timer-plugin', 'xfce4-verve-plugin',
              'xfce4-wavelan-plugin', 'xfce4-weather-plugin',
              'xfce4-whiskermenu-plugin', 'xfce4-xkb-plugin']

os.chdir('../../panel-plugins')

for item in panel_list:
    os.chdir(item)
    os.system('git clone https://gitlab.xfce.org/panel-plugins/' + item)
    os.chdir('../')
