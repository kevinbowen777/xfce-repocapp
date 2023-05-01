#!/usr/bin/env python3

"""
Name: clone_xfce.py
Purpose: Clones Xfce repositories pulled from
           https://gitlab.xfce.org/

source: https://gitlab.com/kevinbowen/xfce-repocapp
version: 0.8.7
updated: 20230314
@author: kevin.bowen@gmail.com
"""

import argparse
import os
import subprocess
import sys
from pathlib import Path

from cappdata import component_list

parser = argparse.ArgumentParser(
    description="clone groups of Xfce components"
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
    help="specify an Xfce component group to clone"
    " from https://gitlab.xfce.org",
)
parser.add_argument("--version", action="version", version="%(prog)s 0.8.7")
args = parser.parse_args()
if args.component is None:
    print(
        "No component was specified. Default to cloning"
        " the 'bindings' components...."
    )
    args.component = "bindings"

line_rule = "\u2248" * 16
path = Path(__file__).parent.resolve()
os.chdir(path)


def clone_xfce(component, comp_list):
    """Run 'git clone' for selected components."""
    print(f"Cloning the Xfce {component} group...")
    # os.chdir(Path(__file__).parent.resolve())

    def get_path(comp_group):
        # grandparent directory (../../) relative to script.
        installpath = Path.cwd().parent.parent.joinpath(comp_group)

        return installpath

    repopath = get_path(component)
    success_count = 0

    os.makedirs(repopath, exist_ok=True)
    os.chdir(repopath)

    for item in component_list(comp_list):
        p = Path(item)
        if p.is_dir():
            print(f"\nThe '{item}' directory already exists. Skipping...\n")
            print(line_rule)
        else:
            try:
                url = f"https://gitlab.xfce.org/{component}/{item}.git"
                subprocess.run(["git", "clone", url], stdout=None, check=True)
                success_count += 1
                print(line_rule)
                print(f"{item} repository cloned successfully.")
            except subprocess.CalledProcessError:
                # On error, returns a non-zero exit status 128.
                print(line_rule)
                print(f"Failed to clone {item} repository.")

            print(
                f"{success_count}/{len(component_list(comp_list))} "
                f"'{component}' repositories cloned successfully."
            )
            print(line_rule)


def main(component_group_name):
    """Build arguments to pass to clone_xfce() with a call to
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
        clone_xfce(
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
