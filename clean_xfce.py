#!/usr/bin/env python3

"""
Name: clean_xfce.py
Purpose: Clean local Xfce repository directories

source: https://gitlab.com/kevinbowen/xfce-repocapp
version: 0.8.4
updated: 20220106
@author: kevin.bowen@gmail.com
"""

import argparse
import os
import sys
import time

from cappdata import component_list

parser = argparse.ArgumentParser(
    description="clean groups of Xfce components")
parser.add_argument("-c", "--component", action='store',
                    choices=['apps', 'bindings', 'xfce', 'panel-plugins',
                             'thunar-plugins', 'all_components'],
                    help="specify a component group to clean")
parser.add_argument('--version', action='version', version='%(prog)s 0.8.4')
args = parser.parse_args()
if args.component is None:
    print("No component was specified. Defaulting to 'apps'.")
    args.component = 'apps'


def clean_xfce(component, comp_list):
    """ Run make clean on component directories. """
    print(f"Cleaning the Xfce {component} group...")
    os.chdir(os.path.dirname(os.path.realpath(__file__)))

    def get_path(comp_group):
        installpath = os.path.abspath(os.path.join(os.getcwd(),
                                                   os.pardir,
                                                   comp_group))

        return installpath

    repopath = get_path(component)
    success_count = 0

    if os.path.isdir(repopath):
        os.chdir(repopath)
        for item in component_list(comp_list):
            if os.path.isdir(item):
                os.chdir(item)
                print('\nCleaning ' + item + ' directory...\n')
                time.sleep(1.5)
                os.system('make -s clean')
                success_count += 1
                print(f"{success_count}/{len(component_list(comp_list))} "
                      f"'{component}' repositories cleaned.")
                print('\nExiting ' + item + ' directory...\n')
                print('\u2248' * 16)
                os.chdir('..')
            else:
                print('\nNothing to do...\n')
                print(f"The '{item}' repository does not exist.\n\n"
                      "Perhaps you need to clone it first.\n")
                print('\u2248' * 16)

    else:
        print('Nothing to do...\n')
        print(f"The '{component}' repositories do not exist.\n\n"
              "Perhaps you need to clone the directory first.\n")
        print('\u2248' * 16)


def main(component_group_name):
    """ Build arguments to pass to clean_xfce() with a call to
    cappdata for component name list.
    command format:
            clean_xfce(component='apps',
                       comp_list='apps')
    """
    cgroup_listname = component_list(component_group_name)
    # All cgroup_listnames will return a string, except 'all'
    if isinstance(cgroup_listname, dict):
        for comp, cglist in cgroup_listname.items():
            clean_xfce(component=comp, comp_list=cglist)
    else:
        clean_xfce(component=component_group_name,
                   comp_list=component_group_name)


if __name__ == '__main__':
    try:
        component_group = args.component
        main(component_group)
    except KeyboardInterrupt:
        print()
        print('Stopped xfce-repocapp. Exiting...')
        sys.exit()
