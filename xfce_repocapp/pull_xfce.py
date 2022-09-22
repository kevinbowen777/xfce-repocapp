#!/usr/bin/env python3

"""
Name: pull_xfce.py
Purpose: update local Xfce repositories pulled from
           https://gitlab.xfce.org

source: https://gitlab.com/kevinbowen/xfce-repocapp
version: 0.8.6
updated: 20220113
@author: kevin.bowen@gmail.com
"""

import argparse
import os
import sys

from cappdata import component_list

parser = argparse.ArgumentParser(
    description="Pull/update groups of Xfce components"
    " from https://gitlab.xfce.org repositories."
)
parser.add_argument(
    "-c",
    "--component",
    action="store",
    choices=[
        "apps",
        "bindings",
        "xfce",
        "panel-plugins",
        "thunar-plugins",
        "www",
        "all_components",
    ],
    help="specify an Xfce component group to pull/update"
    " from https://gitlab.xfce.org.",
)
parser.add_argument("--version", action="version", version="%(prog)s 0.8.6")
args = parser.parse_args()
if args.component is None:
    print(
        "No component was specified. Defaulting to pulling/updating"
        " the 'apps' component repositories."
    )
    args.component = "apps"


def pull_xfce(component, comp_list):
    """Run 'git pull' on selected components to update repositories."""
    print(f"Updating the Xfce {component} group...")
    os.chdir(os.path.dirname(os.path.realpath(__file__)))

    def get_path(comp_group):
        # grandparent directory (../../) relative to script.
        installpath = os.path.abspath(
            os.path.join(os.getcwd(), os.pardir, os.pardir, comp_group)
        )

        return installpath

    repopath = get_path(component)
    success_count = 0

    if os.path.isdir(repopath):
        os.chdir(repopath)
        for item in component_list(comp_list):
            if os.path.isdir(item):
                os.chdir(item)
                print(f"Updating {item}...")
                os.system("git pull")
                success_count += 1
                print(
                    f"\n{success_count}/{len(component_list(comp_list))} "
                    f"'{component}' repositories updated successfully."
                )
                print("\u2248" * 16)
                os.chdir("..")
            else:
                print("\nNothing to do...\n")
                print(
                    f"The '{item}' repository does not exist.\n\n"
                    "Perhaps you need to clone it first.\n"
                )
                print("\u2248" * 16)

    else:
        print("Nothing to do...\n")
        print(
            f"The '{component}' repositories do not exist.\n\n"
            "Perhaps you need to clone the directory first.\n"
        )
        print("\u2248" * 16)


def main(component_group_name):
    """Build arguments to pass to pull_xfce() with a call to
    cappdata for component name list.
    command format:
            pull_xfce(component='apps',
                      comp_list='apps')
    """
    cgroup_listname = component_list(component_group_name)
    # All cgroup_listnames will return a string, except 'all'
    if isinstance(cgroup_listname, dict):
        for comp, cglist in cgroup_listname.items():
            pull_xfce(component=comp, comp_list=cglist)
    else:
        pull_xfce(
            component=component_group_name, comp_list=component_group_name
        )


if __name__ == "__main__":
    try:
        component_group = args.component
        main(component_group)
    except KeyboardInterrupt:
        print()
        print("Stopped xfce-repocapp. Exiting...")
        sys.exit()
