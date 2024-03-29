#!/usr/bin/env python3

import argparse
import os
import sys
from pathlib import Path

from cappdata import component_list, query_yes_no

parser = argparse.ArgumentParser(
    description="Install groups of Xfce components"
    " either locally or system-wide."
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
    help="specify an Xfce component group to install"
    " either locally or system-wide.",
)
parser.add_argument("--version", action="version", version="%(prog)s 0.8.7")
args = parser.parse_args()
if args.component is None:
    print(
        "No component was specified. Default to installation of"
        " the 'apps' components...."
    )
    args.component = "apps"


def install_xfce(component, comp_list):
    """Run 'make install' or 'sudo make install' on selected components."""
    print(f"Installing the Xfce {component} group...")
    os.chdir(Path(__file__).parent.resolve())

    def get_path(comp_group):
        # grandparent directory (../../) relative to script.
        installpath = Path.cwd().parent.parent.joinpath(comp_group)

        return installpath

    repopath = get_path(component)

    if Path.is_dir(repopath):
        os.chdir(repopath)
        for item in component_list(comp_list):
            p = Path(item)
            if p.is_dir():
                os.chdir(item)
                confirm = query_yes_no(
                    f"Do you want to install '{item}' to the system? "
                    f"Answer 'No' to install locally. "
                )
                if confirm == "yes":
                    print(f"Installing {item} to the system...")
                    os.system("sudo make install")
                    print("\u2248" * 16)
                    os.chdir("..")
                else:
                    print(f"Installing {item} locally...")
                    os.system("make install")
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
    """Build arguments to pass to install_xfce() with a call to
    cappdata for component name list.
    command format:
            install_xfce(component='apps',
                         comp_list='apps')
    """
    cgroup_listname = component_list(component_group_name)
    # All cgroup_listnames will return a string, except 'all'
    if isinstance(cgroup_listname, dict):
        for comp, cglist in cgroup_listname.items():
            install_xfce(component=comp, comp_list=cglist)
    else:
        install_xfce(
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
