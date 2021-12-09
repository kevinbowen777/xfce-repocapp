# xfce-repocapp - TODO

----

### as of 20210109
 - fix pull_core.py update delimers
 - fix typos in README
 - add banner to build menu that this assumes that all build
    requirements have already been handled and is not addressed by
    this app
 - add banner to install menu indicating that 'build' needs to
    be run first
 - Update README with instructions for changing install
    directory
 - Move repo URLs into cappdata.py module?
 - add final successful count of cloned repos
 - remove __init__.py ??
 - add __init__.main() on individual scripts???
 - add 'performing x action on component' in main() for running standalone scripts
   - or move from xfce-repocapp.sh into body of script
 - improve main menu (xfce-repocapp.sh)
   - which library?
   - improve menu selection
     - allow words and first letter of actions 

   - rewrite main menu in Python
     - build
     - clean
     - clone
     - install
     - pull
     - purge
 - write tests
   - main menu(xfce-repocapp.sh)
   - 
 - provide summary of actions upon completion
 - package for TestPy/PyPi
---
### as of 20210108
 - ~~add branch indicator to main menu (xfce-repocapp.sh)~~
 - fix typos in README
 - add banner to build menu that this assumes that all build
    requirements have already been handled and is not addressed by
    this app
 - add banner to install menu indicating that 'build' needs to
    be run first
 - ~~add exception handling for changing into non-existent 
    directories~~
 - Update README with instructions for changing install
    directory
 - Move repo URLs into cappdata.py module?
 - add final successful count of cloned repos
 - ~~add count for cloning core, panel-plugins~~
 - remove __init__.py ??
 - ~~check for directory existence in pull scripts~~
   - ~~add update count for same~~
 - ~~check for directory existence in clean scripts~~
   - ~~add update count for same~~
 - ~~check for directory existence in install scripts~~
 - - ~~add update count for same~~
 - ~~allow for choice in system vs. local install scripts (sudo vs. no-sudo)~~
 - add __init__.main() on individual scripts???
 - add 'performing x action on component' in main() for running standalone scripts
   - or move from xfce-repocapp.sh into body of script
 - improve main menu (xfce-repocapp.sh)
   - which library?
   - improve menu selection
     - allow words and first letter of actions 

   - rewrite main menu in Python
 - ~~move packages into single file in parent directory~~
   - clean up path manipulation in individual scripts
     - build
     - clean
     - clone
     - install
     - pull
     - purge
 - write tests
   - main menu(xfce-repocapp.sh)
   - 
 - provide summary of actions upon completion
 - package for TestPy/PyPi
