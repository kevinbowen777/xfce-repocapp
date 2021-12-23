>>>>># xfce-repocapp - TODO

### Current TODO list
 - tag 0.8.1
 - update README
 - add CHANGELOG to master
 - rewrite main menu in Python
 - write tests
 - improve main menu (`xfce-repocapp.sh`)
   - rewrite in python  
 - add final successful count of actions when using `all`

----

### as of 20211220
 - tag 0.8.1
 - update README
 - add CHANGELOG to master
 - rewrite main menu in Python
 - write tests
 - improve main menu (`xfce-repocapp.sh`)
   - rewrite in python  
 - add final successful count of actions when using `all`**

### as of 20211215
 - ~~merge current dev branch with master~~
 - ~~tag 0.7.1 release~~

 - ~~build dev branch for preparation for upload to PyTest~~
    - ~~create toml~~
    - ~~change setup.py to setup.cfg~~
 - ~~FEATURE improvement: return to main menu after a 'non-all' command?~~
 - ~~change `echo` statements to `printf` for more reliable behavior~~
 - ~~fix `FileNotFound` bug with `build` when component dir is missing~~
 - ~~fix silent failure bug with `clean` doesn't generate an error
    when component dir is missing~~
 - ~~clean up & standardize path manipulation behavior~~
 - ~~fix `pull_<xxx>.py` update delimiters~~
 - ~~Update `README.md` with instructions for changing install
    directory~~
 - add final successful count of cloned repos
 - ~~add __init__.main() on individual scripts~~
 - ~~add 'performing x action on component' in main() for running standalone scripts~~
   - ~~or move from `xfce-repocapp.sh` into body of script~~
 - improve main menu (`xfce-repocapp.sh`)
   - which library? (argparse/Click?)
     - convert .sh file to .py
     - prefer _not_ to rely on 3rd party libs
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
   - main menu(`xfce-repocapp.sh`)
   - 
 - provide summary of actions upon completion

----
### as of 20211209
 - change `echo` statements to `printf` for more reliable behavior
 - ~~fix `FileNotFound` bug with `build` when component dir is missing~~
 - ~~fix silent failure bug with `install` doesn't generate an error 
   ~~when component dir is missing~~
 - ~~fix silent failure bug with`pull` doesn't generate an error~~
    ~~when component dir is missing~~
 - ~~fix silent failure bug with `clean` doesn't generate an error~~
    ~~when component dir is missing~~
 - clean up & standardize path manipulation behavior
 - look into using pathlib to get rid of `repodir()` in `cappdata.py`
 - ~~add installation instructions to`README.md`
   ~~note difference between master & dev branches(including use of pip)~~
 - fix `pull_<xxx>.py` update delimiters
 - ~~fix typos in README~~
 - Update `README.md` with instructions for changing install
    directory
 - Move repo URLs into `cappdata.py` module?
 - add final successful count of cloned repos
 - add __init__.main() on individual scripts???
 - add 'performing x action on component' in main() for running standalone scripts
   - or move from `xfce-repocapp.sh` into body of script
 - improve main menu (`xfce-repocapp.sh`)
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
   - main menu(`xfce-repocapp.sh`)
   - 
 - provide summary of actions upon completion
 - package for TestPy/PyPi
---
### as of 20211208
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
 - ~~remove __init__.py~~
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
=======
----
 - add branch indicator to main menu (xfce-repocapp.sh)
 - fix typos in README
 - improve main menu (xfce-repocapp.sh)
   - which library?
   - improve menu selection
     - allow words and first letter of actions
     - 
   - rewrite main menu in Python
 - move packages into single file in parent directory
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

