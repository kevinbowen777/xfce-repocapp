#!/usr/bin/env python3

# ---------------------------------------------------------------------- #
#
# Name: purge_xfce_panel_plugins.py
# Purpose: delete the local Xfce panel-plugins repositories pulled from
#           https://gitlab.xfce.org/panel-plugins
#
# version: 0.3
# updated: 20210130
# @author: kevin.bowen@gmail.com
#
# ---------------------------------------------------------------------- #

import os

xfce_panel_plugins_list = ['xfce4-battery-plugin', 'xfce4-calculator-plugin',
                            'xfce4-clipman-plugin', 'xfce4-cpufreq-plugin',
                            'xfce4-cpugraph-plugin', 'xfce4-datetime-plugin',
                            'xfce4-diskperf-plugin', 'xfce4-embed-plugin',
                            'xfce4-eyes-plugin', 'xfce4-fsguard-plugin',
                            'xfce4-genmon-plugin', 'xfce4-indicator-plugin',
                            'xfce4-mailwatch-plugin', 'xfce4-mount-plugin',
                            'xfce4-mpc-plugin', 'xfce4-netload-plugin',
                            'xfce4-notes-plugin', 'xfce4-places-plugin',
                            'xfce4-pulseaudio-plugin', 'xfce4-sample-plugin',
                            'xfce4-sensors-plugin',
                            'xfce4-smartbookmark-plugin',
                            'xfce4-statusnotifier-plugin',
                            'xfce4-stopwatch-plugin',
                            'xfce4-systemload-plugin', 'xfce4-time-out-plugin',
                            'xfce4-timer-plugin', 'xfce4-verve-plugin',
                            'xfce4-wavelan-plugin', 'xfce4-weather-plugin',
                            'xfce4-whiskermenu-plugin', 'xfce4-xkb-plugin']

confirm = input('Are you sure you want to remove the Xfce panel-plugins'
                ' repositories? ')
if confirm.lower() == 'yes':
    for item in xfce_panel_plugins_list:
        os.system('rm -rf ../panel-plugins/' + item)
        print("The " + item + " Xfce panel-plugin repo has been purged.")
    os.system('rmdir ../panel-plugins/')
    print('The panel-plugins directory has been deleted.')
else:
    print("No repositories have been deleted. Have a nice day.")
