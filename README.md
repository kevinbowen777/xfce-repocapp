<div align="center">

  [![Status](https://img.shields.io/badge/status-active-success.svg)]()
  [![GitHub Issues](https://img.shields.io/github/issues/kevinbowen777/xfrepos.svg)](https://github.com/kevinbowen777/xfrepos/issues)
  [![License](https://img.shields.io/badge/License-GPL%20v2-blue.svg)](https://gitlab.com/kevinbowen/xfrepos/-/blob/master/LICENSE)
  [![Coverage](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/kevinbowen777/e1cbfcb69276c8b91e37a811b9fab725/raw/xfrepos_covbadge.json)](https://kevinbowen777.github.io/xfrepos/)

</div>

# xfrepos

A collection of scripts to maintain local Xfce repositories.

The purpose of the scripts contained in the `xfrepos` repository is to
facilitate the management of local Xfce repositories in bulk.
Cloning, building repositories, installing, purging and updating tasks are
performed in groups, organized by categories, according to the official
Xfce repository structure (https://gitlab.xfce.org).


   * [List of scripts](#list-of-scripts)
     * [Menu scripts](#menu-scripts)
     * [Individual action scripts](#individual-action-scripts)
     * [Running individual scripts](#running-individual-scripts)
   * [Installation of xfrepos project](#installation-of-xfrepos-project)
   * [List of repository mirrors](#list-of-repository-mirrors)
   * [Reporting Bugs](#reporting-bugs)

----
### List of scripts
#### Menu scripts
`xfrepos.py` - provides a rudimentary menu-driven option to run the scripts.
  This is entirely optional. All of these scripts can be run independently.

----
#### Individual action scripts

 - `clone_xfce.py` - Clone Xfce repositories from https://gitlab.xfce.org
 - `build_xfce.py` - Compile local component repositories

**N.B.: These scripts perform _ABSOLUTELY NO CHECKS_ for missing system libraries or the
order of component compilation. It is assumed that you know what you are
doing. Use at your own risk. No guarantees.**

For additional information on building Xfce see: https://docs.xfce.org/xfce/building
 - `pull_xfce.py` - Update local component repositories with git pull
 - `purge_xfce.py` - Delete local component repositories by category
 - `install_xfce.py` - Install components locally or system-wide with `sudo make install`
 - `clean_xfce.py` - Clean local component directories (make clean)

#### Running individual scripts
All of the *-xfce.py scripts take the argument `-c` and the name of the
component group to be acted upon. The following names are used:
 - apps
 - bindings
 - xfce
 - panel-plugins
 - thunar-plugins
 - www
 - all

For example:
 - `clone_xfce.py -c panel-plugins`
 - `purge_xfce.py -c all`

Running the script without an argument will, by default, act upon the `apps`
components(e.g. `pull_xfce -c apps`).

----

### Installation of xfrepos project

    git clone https://github.com/kevinbowen777/xfrepos.git

----
### List of repository mirrors

- https://github.com/kevinbowen777/xfrepos
- https://gitlab.com/kevinbowen/xfrepos
- https://codeberg.org/kevinbowen/xfrepos
- http://bitbucket.org/kevinbowen/xfrepos

----
### Reporting Bugs

   Visit the [Issues page](https://github.com/kevinbowen777/xfrepos/issues)
     to view currently open bug reports or open a new issue.
