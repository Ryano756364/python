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