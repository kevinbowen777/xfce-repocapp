#!/usr/bin/env python3

import argparse
import os
import sys
import time
from pathlib import Path

from cappdata import component_list

parser = argparse.ArgumentParser(
    description="Build groups of Xfce components locally."
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
    help="Specify an Xfce component group to build locally.",
)
parser.add_argument("--version", action="version", version="%(prog)s 0.8.7")
args = parser.parse_args()
if args.component is None:
    print(
        "No component was specified. Default to building"
        " the 'apps' components locally...."
    )
    args.component = "apps"

line_rule = "\u2248" * 16
path = Path(__file__).parent.resolve()
os.chdir(path)


def build_xfce(component, comp_list):
    """Run autogen.sh and make on selected components."""
    print(f"Building the Xfce {component} group...")

    def get_path(comp_group):
        # grandparent directory (../../) relative to script.
        installpath = Path.cwd().parent.parent.joinpath(comp_group)

        return installpath

    repopath = get_path(component)
    os.environ["PKG_CONFIG_PATH"] = "/usr/lib/pkgconfig:/usr"

    if Path.is_dir(repopath):
        os.chdir(repopath)
        for item in component_list(comp_list):
            p = Path(item)
            if p.is_dir():
                os.chdir(item)
                print(f"\nRunning autogen.sh for {item} ...\n")
                os.system("./autogen.sh --prefix=/usr")
                print(f"\nRunning make for {item} ...\n")
                time.sleep(1.5)
                os.system("make")
                os.chdir("..")
            else:
                print("\nNothing to do...\n")
                print(
                    f"The '{item}' repository does not exist.\n\n"
                    "Perhaps you need to clone it first.\n"
                )
                print(line_rule)

    else:
        print("Nothing to do...\n")
        print(
            f"The '{component}' repositories do not exist.\n\n"
            "Perhaps you need to clone the directory first.\n"
        )
        print(line_rule)


def main(component_group_name):
    """Build arguments to pass to build_xfce() with a call to
    cappdata for component name list.
    command format:
            build_xfce(component='apps',
                       comp_list='apps')
    """
    cgroup_listname = component_list(component_group_name)
    # All cgroup_listnames will return a string, except 'all'
    if isinstance(cgroup_listname, dict):
        for comp, cglist in cgroup_listname.items():
            build_xfce(component=comp, comp_list=cglist)
    else:
        build_xfce(
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
