#!/usr/bin/env python3

"""
Name: purge_xfce.py
Purpose: delete the local Xfce repositories originally pulled from
           https://gitlab.xfce.org

source: https://gitlab.com/kevinbowen/xfce-repocapp
version: 0.8.4
updated: 20220106
@author: kevin.bowen@gmail.com
"""

import argparse
import os
import shutil
import sys

from cappdata import component_list
from cappdata import query_yes_no

parser = argparse.ArgumentParser(
    description='Purge(Delete) groups of local Xfce component directories.')
parser.add_argument('-c', '--component',
                    action='store',
                    choices=['apps',
                             'bindings',
                             'xfce',
                             'panel-plugins',
                             'thunar-plugins',
                             'www',
                             'all_components'],
                    help='Specify an Xfce component group to delete.')
parser.add_argument('--version',
                    action='version',
                    version='%(prog)s 0.8.4')
args = parser.parse_args()
if args.component is None:
    print("No component was specified.\nPlease specify a component group'"
          " to delete with the '-c' option.")
    sys.exit()


def purge_xfce(component, comp_list):
    """ Delete files and directories of selected components. """
    print(f"Purging the Xfce {component} group...")
    os.chdir(os.path.dirname(os.path.realpath(__file__)))

    def get_path(comp_group):
        installpath = os.path.abspath(os.path.join(os.getcwd(),
                                                   os.pardir,
                                                   comp_group))

        return installpath

    repopath = get_path(component)
    success_count = 0

    confirm = query_yes_no(f"Are you sure you want to remove the "
                           f"Xfce '{component}' repositories? ")

    if confirm == 'yes':
        if os.path.isdir(repopath):
            os.chdir(repopath)
            for item in component_list(comp_list):
                if os.path.isdir(item):
                    try:
                        shutil.rmtree(item)
                        success_count += 1
                        print(f"\nThe '{item}' directory has been deleted.\n")
                        print(f"{success_count}"
                              f"/{len(component_list(comp_list))} "
                              f"'{component}' repositories deleted "
                              f"successfully.")
                        print('\u2248' * 16)
                    except FileNotFoundError:
                        print(f"The directory '{item}' does not exist. "
                              f"Skipping...")
                        print('\u2248' * 16)
            os.chdir('..')
            shutil.rmtree(component)
            print(f"\nThe directory '{component}' has been deleted.\n")
            print('\u2248' * 16)
        else:
            print('Nothing to do...\n')
            print(f"The '{component}' repositories do not exist.\n\n"
                  "Perhaps you need to clone the directory first.\n")
            print('\u2248' * 16)

    else:
        print("No repositories have been deleted. Have a nice day.")


def main(component_group_name):
    """ Build arguments to pass to purge_xfce() with a call to
    cappdata for component name list.
    command format:
            pull_xfce(component='apps',
                      comp_list='apps')
    """
    cgroup_listname = component_list(component_group_name)
    # All cgroup_listnames will return a string, except 'all'
    if isinstance(cgroup_listname, dict):
        for comp, cglist in cgroup_listname.items():
            purge_xfce(component=comp, comp_list=cglist)
    else:
        purge_xfce(component=component_group_name,
                   comp_list=component_group_name)


if __name__ == '__main__':
    try:
        component_group = args.component
        main(component_group)
    except KeyboardInterrupt:
        print()
        print('Stopped xfce-repocapp. Exiting...')
        sys.exit()
