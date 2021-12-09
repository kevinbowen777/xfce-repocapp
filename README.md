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

`xfce-repocapp.sh` provides a rudimentary menu-driven option to run the scripts.
    This is entirely optional. All of the scripts can be run independently.


----
### Clone scripts

        Clone Xfce repositories from https://gitlab.xfce.org

 - clone_all.py
 - clone_apps.py
 - clone_bindings.py
 - clone_core.py
 - clone_panel_plugins.py
 - clone_thunar_plugins.py
 - clone_www.py

----
### Autogen (Build) scripts

        Run autogen & make against local component repositories

**N.B.: These scripts perform _ABSOLUTELY NO CHECKS_ for missing system libraries or the
order of component compilation. It is assumed that you know what you are
doing. Use at your own risk. No guarantees.**

For additional information on building Xfce see: https://docs.xfce.org/xfce/building

 - build_all.py
 - build_apps.py
 - build_bindings.py
 - build_core.py
 - build_panel_plugins.py
 - build_thunar_plugins.py

----
### Pull (Update) scripts

         Update local component repositories with git pull

 - pull_all.py
 - pull_apps.py
 - pull_bindings.py
 - pull_core.py
 - pull_panel_plugins.py
 - pull_thunar_plugins.py
 - pull_www.py

----
### Purge scripts

        Delete local component repositories by category

 - purge_all.py
 - purge_apps.py
 - purge_core.py
 - purge_bindings.py
 - purge_panel_plugins.py
 - purge_thunar_plugins.py
 - purge_www.py

----

### Installation scripts

          Install components locally or system-wide with sudo make install

 - install_all.py
 - install_apps.py
 - install_bindings.py
 - install_core.py
 - install_panel_plugins.py
 - install_thunar_plugins.py

----

### Clean scripts

          Clean local component directories (make clean)

 - clean_all.py
 - clean_apps.py
 - clean_bindings.py
 - clean_core.py
 - clean_panel_plugins.py
 - clean_thunar_plugins.py

----

### Installation of xfce-repocapp project

    Main: git clone https://gitlab.com/kevinbowen/xfce-repocapp.git
    Mirror: git clone https://github.com/kevinbowen777/xfce-repocapp.git

----
### Reporting Bugs

   Visit the [Issues page](https://gitlab.com/kevinbowen/xfce-repocapp/-/issues)
     to view currently open bug reports or open a new issue.
