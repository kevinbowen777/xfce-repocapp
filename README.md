[![License](https://img.shields.io/badge/License-GPL%20v2-blue.svg)](https://gitlab.com/kevinbowen/xfce-repocapp/-/blob/master/LICENSE)

# Xfce-repocapp

repocapp - repository (C)lone (A)utogen (P)ull (P)urge
              (This also includes clean & installation scripts)

A collection of scripts to maintain local Xfce repositories.

The purpose of the scripts contained in the `xfce-repocapp` repository is to
facilitate managing your local Xfce repositories in bulk.
Cloning, running automake, installing, purging and updating tasks are
performed in groups, organized by categories, according to the official
Xfce repository structure (https://gitlab.xfce.org).

----
### List of scripts
#### Menu scripts
`xfce-repocapp.py` - provides a rudimentary menu-driven option to run the scripts.
  This is entirely optional. All of these scripts can be run independently.

----
#### Individual action scripts 

 - `clone_xfce.py` - Clone Xfce repositories from https://gitlab.xfce.org
 - `build_xfce.py` - Run autogen & make against local component repositories
 
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
components. This is the equivalent of running, for example, `pull_xfce -c apps`.

----

### Installation of xfce-repocapp project

    Master: git clone https://gitlab.com/kevinbowen/xfce-repocapp.git
    Mirror: git clone https://github.com/kevinbowen777/xfce-repocapp.git



----
### Reporting Bugs

   Visit the [Issues page](https://gitlab.com/kevinbowen/xfce-repocapp/-/issues)
     to view currently open bug reports or open a new issue.
