# Introduction

General learning of Python with notes and practice problems.

## Resources used

Dead Simple Python - Jason C. McDonald 2023

## Notes

* Running python files in command line (not the interpreter)
  * python3 myfile.py
* Package
* collection of code, which is analogous to a library in most other programming languages
* Virtual environment
  * sandbox where you can install only the Python packages you need for a particular project, without the risk of those packages clashing with those for another project (or your system)
  * Creating virtual environment
    * conventional file names are usually env or venv
    * Python provides a tool called **venv**
      > python3 -m venv venv
    * venv first one is command that creates virtual environment
    * second venv is the path (this one happens to be a relative path)
    * absolute path would work too
    * if older version of python is being used
      > virtualenv -p python3 venv
* Activate virtual environment
  * on Windows
    > venv/Scripts/activate.bet
  * To close
    > venv/Scripts/deactivate.bat
* pip
  * **package manager**
  * Remember, for any Python development work, you should almost always work in virtual environments
  * for system-wide packages, make sure you are *not* in virtual environment
    > python3 -m pip *command*
  * command explanations coming soon
* Installing packages
  > pip install *package*
* Requirements.txt file
  * could be helpful to include for myself or others when creating a program
  * lists the packages your project needs
  * when creating a virtual environment, me or others can install all the requirement packages with a single command
  * the command to run all those packages would be
    > pip install -r requirements.txt
* Caution with packages
  * when removing packages be careful not to delete packages that may have dependency-related issues
  * use virtual machine to test out this and delete virtual sandbox if error occurs with removing package
* Find packages
  > pip search web scraping
  * or https://pypi.org is the official Python Package Index
  * **never** use 
    > sudo pip
  * on UNIX-like systems
  * instead replace
    > sudo pip
    * with
    > python3 -m pip
    * or
    > > pip install --user
    * to install to their local directory
* VE + Git
  * tricky.
  * Two options:
    * (1) Create virtual environments outside your repository
    * (2) Untrack the virtual environment directory in the VCS
  * arguments in favor of both rules
* Shebang
  * Strongly recommended to add a shebang line at top of a Python file so that file can be directly executable
  * for Python 3
    > #!/usr/bin/env python3
  * for *both* python2 and python3
    > #!/usr/bin/env python
* Virtual Environment Tips and Tricks
  * You can use binaries that are a part of the VE without activating it
    * assuming VE is **venv**
      > venv/bin/pip install pylint
      > venv/bin/python
      > .
      > import pylint
    * this works! will not be system wide unless you installed pylint for the whole system
  * Most used in this book:
    * pip and venv
    * alternatives worth looking into:
      * Pipenv
        * combines both pip and venv into one cohesive tool
        * not covered in this book
        * https://docs.pipenv.org/
      * pip-tools
        * use only within virtual environments as it's designed specifically for that use case
        * https://pypi.org/project/pip-tools/
      * poetry
        * some developers hate pip altogether
        * poerty is an alternative package manager
        * don't use pip to install it
        * https://python-poetry.org/
* PEP 8
  * Python's official style guide known as *PEP 8*
  * not mandatory for a project but should be followed
  * consistency of style in a project or design is the most important
* 80/100
  * Try to keep characters on line limited to 80 but hard cutoff should be 100
* Spaces
  * PEP 8 recommends spaces over tabs, techincally
  * at least don't mix the two
  * use one or the other and stick throughout project that way
  * if spaces, are used
    * use 4
  * most code editors use 4 spaces for tabs anyway
* Static analyzer
  * one most common type is a *linter*
  * for python:
    * *Pylint* and *PyFlakes*
  * Additional support
    * *Mypy* and *mccabe*
* Autoformatting tools
  * *autopep8*
  * to fix most PEP 8 issues, run this
    > autopep8 --in-place --aggressive --aggressive *filetochange.py*
  * *black*
    * install this with pip as well
    * simpler
      > black filetochange.py
* Testing frameworks
  * Recommended:
    * *Pytest*
    * *nose2*
    * *unittest*
    * all of these are installed with pip
* 