#!/usr/bin/env python3

"""
Name: clone_xfce.py
Purpose: Clones Xfce repositories pulled from
           https://gitlab.xfce.org/

source: https://gitlab.com/kevinbowen/xfce-repocapp
version: 0.8.5
updated: 20220113
@author: kevin.bowen@gmail.com
"""

import argparse
import os
import subprocess
import sys

from cappdata import component_list

parser = argparse.ArgumentParser(
    description='clone groups of Xfce components'
                ' from https://gitlab.xfce.org repositories.')
parser.add_argument('-c', '--component',
                    action='store',
                    choices=['apps',
                             'bindings',
                             'xfce',
                             'panel-plugins',
                             'thunar-plugins',
                             'www',
                             'all_components'],
                    help='specify an Xfce component group to clone'
                         ' from https://gitlab.xfce.org')
parser.add_argument('--version',
                    action='version',
                    version='%(prog)s 0.8.5')
args = parser.parse_args()
if args.component is None:
    print("No component was specified. Default to cloning"
          " the 'apps' components....")
    args.component = 'apps'


def clone_xfce(component, comp_list):
    """ Run 'git clone' for selected components. """
    print(f"Cloning the Xfce {component} group...")
    os.chdir(os.path.dirname(os.path.realpath(__file__)))

    def get_path(comp_group):
        installpath = os.path.abspath(os.path.join(os.getcwd(),
                                                   os.pardir,
                                                   comp_group))

        return installpath

    repopath = get_path(component)
    success_count = 0

    os.makedirs(repopath, exist_ok=True)
    os.chdir(repopath)

    for item in component_list(comp_list):
        if os.path.isdir(item):
            print(f"\nThe '{item}' directory already exists. Skipping...\n")
            print('\u2248' * 16)
        else:
            try:
                url = f"https://gitlab.xfce.org/{component}/{item}.git"
                print(subprocess.check_output(['git', 'clone', url],
                      stderr=subprocess.STDOUT,
                      text=True))
                success_count += 1
                print('\u2248' * 16)
                print(f"{item} repository cloned successfully.")
            except subprocess.CalledProcessError:
                # On error, returns a non-zero exit status 128.
                print('\u2248' * 16)
                print(f"Failed to clone {item} repository.")

            print(f"{success_count}/{len(component_list(comp_list))} "
                  f"'{component}' repositories cloned successfully.")
            print('\u2248' * 16)


def main(component_group_name):
    """ Build arguments to pass to clone_xfce() with a call to
    cappdata for component name list.
    command format:
            clone_xfce(component='apps',
                       comp_list='apps')
    """
    cgroup_listname = component_list(component_group_name)
    # All cgroup_listnames will return a string, except 'all'
    if isinstance(cgroup_listname, dict):
        for comp, cglist in cgroup_listname.items():
            clone_xfce(component=comp, comp_list=cglist)
    else:
        clone_xfce(component=component_group_name,
                   comp_list=component_group_name)


if __name__ == '__main__':
    try:
        component_group = args.component
        main(component_group)
    except KeyboardInterrupt:
        print()
        print('Stopped xfce-repocapp. Exiting...')
        sys.exit()
