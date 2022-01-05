#!/usr/bin/env python3

"""
Name: cappdata.py
Purpose: component lists and query function for use with
           xfce-repocapp.py and associated scripts

source: https://gitlab.com/kevinbowen/xfce-repocapp
version: 0.8.4
updated: 20220101
@author: kevin.bowen@gmail.com
"""

import sys
import tty
import termios


def apps_list():
    """ https://gitlab.xfce.org/apps """
    apps = ['catfish', 'gigolo', 'mousepad', 'parole', 'ristretto',
            'xfburn', 'xfce4-dict', 'xfce4-mixer', 'xfce4-notifyd',
            'xfce4-panel-profiles', 'xfce4-screensaver',
            'xfce4-screenshooter', 'xfce4-taskmanager', 'xfce4-terminal',
            'xfce4-volumed-pulse', 'xfdashboard', 'xfmpc']
    return apps


def bindings_list():
    """ https://gitlab.xfce.org/bindings """
    bindings = ['thunarx-python', 'xfce4-vala']
    return bindings


def core_list():
    """ https://gitlab.xfce.org/xfce """
    core = ['exo', 'garcon', 'libxfce4ui', 'libxfce4util',
            'thunar', 'thunar-volman', 'tumbler', 'xfce4-appfinder',
            'xfce4-dev-tools', 'xfce4-panel', 'xfce4-power-manager',
            'xfce4-session', 'xfce4-settings', 'xfconf', 'xfdesktop', 'xfwm4']
    return core


def panel_plugins_list():
    """ https://gitlab.xfce.org/panel-plugins """
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
                     'xfce4-statusnotifier-plugin', 'xfce4-stopwatch-plugin',
                     'xfce4-systemload-plugin', 'xfce4-time-out-plugin',
                     'xfce4-timer-plugin', 'xfce4-verve-plugin',
                     'xfce4-wavelan-plugin', 'xfce4-weather-plugin',
                     'xfce4-whiskermenu-plugin', 'xfce4-xkb-plugin']
    return panel_plugins


def thunar_plugins_list():
    """ https://gitlab.xfce.org/thunar-plugins """
    thunar_plugins = ['thunar-archive-plugin', 'thunar-media-tags-plugin',
                      'thunar-shares-plugin', 'thunar-vcs-plugin']
    return thunar_plugins


def www_list():
    """ https://gitlab.xfce.org/www """
    www = ['archive.xfce.org', 'blog.xfce.org', 'cdn.xfce.org',
           'forum.xfce.org', 'moka', 'wiki.xfce.org', 'www.xfce.org']
    return www


def press_any_key():
    """ Doesn't work for shift/control keys."""
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        return sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)


def query_yes_no(question, default="yes"):
    """ Handles confirmation prompts. """
    valid = {'yes': 'yes', 'y': 'yes', 'ye': 'yes',
             'no': 'no', 'n': 'no'}
    if default is None:
        prompt = ' [(Y)es/(N)o] '
    elif default == 'yes':
        prompt = ' ([Y]es/[N]o) '
    elif default == 'no':
        prompt = ' [y/N] '
    else:
        raise ValueError(f"invalid default answer: {default}")

    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == '':
            return default
        elif choice in valid.keys():
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")


if __name__ == '__main__':
    pass
