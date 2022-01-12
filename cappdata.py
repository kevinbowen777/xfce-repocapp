#!/usr/bin/env python3

"""
Name: cappdata.py
Purpose: component lists and query function for use with
           xfce-repocapp.py and associated scripts

source: https://gitlab.com/kevinbowen/xfce-repocapp
version: 0.8.5
updated: 20220111
@author: kevin.bowen@gmail.com
"""

import sys
import tty
import termios


def component_list(component_group_list):
    """returns lists of components."""
    if component_group_list == 'apps':
        apps = ['catfish', 'gigolo', 'mousepad', 'parole', 'ristretto',
                'xfburn', 'xfce4-dict', 'xfce4-mixer', 'xfce4-notifyd',
                'xfce4-panel-profiles', 'xfce4-screensaver',
                'xfce4-screenshooter', 'xfce4-taskmanager', 'xfce4-terminal',
                'xfce4-volumed-pulse', 'xfdashboard', 'xfmpc',
                ]
        return apps

    if component_group_list == 'bindings':
        bindings = ['thunarx-python', 'xfce4-vala']
        return bindings

    if component_group_list == 'xfce':
        xfce = ['exo', 'garcon', 'libxfce4ui', 'libxfce4util',
                'thunar', 'thunar-volman', 'tumbler', 'xfce4-appfinder',
                'xfce4-dev-tools', 'xfce4-panel', 'xfce4-power-manager',
                'xfce4-session', 'xfce4-settings', 'xfconf', 'xfdesktop',
                'xfwm4',
                ]
        return xfce

    if component_group_list == 'panel-plugins':
        panel_plugins = ['xfce4-battery-plugin', 'xfce4-calculator-plugin',
                         'xfce4-clipman-plugin', 'xfce4-cpufreq-plugin',
                         'xfce4-cpugraph-plugin', 'xfce4-datetime-plugin',
                         'xfce4-diskperf-plugin', 'xfce4-docklike-plugin',
                         'xfce4-embed-plugin', 'xfce4-eyes-plugin',
                         'xfce4-fsguard-plugin', 'xfce4-genmon-plugin',
                         'xfce4-indicator-plugin', 'xfce4-mailwatch-plugin',
                         'xfce4-mount-plugin', 'xfce4-mpc-plugin',
                         'xfce4-netload-plugin', 'xfce4-notes-plugin',
                         'xfce4-places-plugin',  'xfce4-pulseaudio-plugin',
                         'xfce4-sample-plugin', 'xfce4-sensors-plugin',
                         'xfce4-smartbookmark-plugin',
                         'xfce4-statusnotifier-plugin',
                         'xfce4-stopwatch-plugin', 'xfce4-systemload-plugin',
                         'xfce4-time-out-plugin', 'xfce4-timer-plugin',
                         'xfce4-verve-plugin', 'xfce4-wavelan-plugin',
                         'xfce4-weather-plugin', 'xfce4-whiskermenu-plugin',
                         'xfce4-xkb-plugin',
                         ]
        return panel_plugins

    if component_group_list == 'thunar-plugins':
        thunar_plugins = ['thunar-archive-plugin', 'thunar-media-tags-plugin',
                          'thunar-shares-plugin', 'thunar-vcs-plugin',
                          ]
        return thunar_plugins

    if component_group_list == 'www':
        www = ['archive.xfce.org', 'blog.xfce.org', 'cdn.xfce.org',
               'forum.xfce.org', 'moka', 'wiki.xfce.org', 'www.xfce.org',
               ]
        return www

    if component_group_list == 'all_components':
        all_components = {'apps': 'apps',
                          'bindings': 'bindings',
                          'xfce': 'xfce',
                          'panel-plugins': 'panel-plugins',
                          'thunar-plugins': 'thunar-plugins',
                          'www': 'www',
                          }
        return all_components


def press_any_key():
    """ Doesn't work for shift/control keys."""
    file_descriptor = sys.stdin.fileno()
    tty_attributes = termios.tcgetattr(file_descriptor)
    try:
        print("Press any to continue...")
        tty.setraw(file_descriptor)
        return sys.stdin.read(1)
    finally:
        termios.tcsetattr(file_descriptor, termios.TCSADRAIN, tty_attributes)


def query_yes_no(question, answer='no'):
    """
    Handles confirmation prompts. Used in install_xfce.py
    and purge_xfce.py
    """
    valid = {'yes': 'yes', 'y': 'yes',
             'no': 'no', 'n': 'no'}
    prompt = ' [(Y)es/(N)o/Default: No] '

    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        try:
            if answer is not None and choice == '':
                return answer
            elif answer in valid:
                return valid[choice]
        except KeyError:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")


if __name__ == '__main__':
    pass
