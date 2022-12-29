# Setting up Projects

## Modules and packages

### Modules

- any .py file
- actually objects, not just files

### Package

- one or more modules within a directory
- the directory must include a __ init __.py file which can be empty
  - if it isn't placed there then Python won't know that the directory consitutes a package
- files too, but with a __ path __ attribute
- will matter more between the disctinction of the two once import systems are discussed

### Naming conventions
- should have short and all lowercase 
- use of underscores is discouraged

## How Importing Works
    import re

## Import Dos and Don'ts
    #1!/usr/bin/env python3

    def open():
        #does something
    def close():
        #does something

    -----
    import smart_door
    smart_door.open()
    smart_door.close()

* the *namespace* of open and close is smart_door
* **namespace**
  * an explicitly defined path to something, such as a function
* Python loves namespaces

### To avoid typing namespace over and over again
    from smart_door import open
    open()
    
    from smart_door import open, close
    open()
    close()

### But open() is a built-in function already in Python and may cause issues, so...
    from smart_door import open as door_open
    from smart_door import close

    door_open()
    close()

* The double use of open() is called shadowing

### Nesting packages
    import omission.data.data_loader

* Python interpreter looks for the omission package
  * then the data package inside that
    * then the data_loader module inside that

* try to keep projects 2-3 levels deep so as to avoid a situation like
  > from musicapp.player.data.library import song
* but sometimes it can't be avoided to follow the Python Zen of 
  * Flat is better than nested

### Beware of importing all
    from smart_door import *

* ***very bad idea***
* can be troublesome if importing all from many modules and there is a similar functions being called

### Absolute imports
    from omission.common.game_enums import GameMade

* omission is the top level package

### Relative imports
    from ..common.game_enums import GameMade

* there is debate whether to use relative or absolute
* big thing is to make it clear where anything comes from
* ...but maybe use absolute if there was a choice

### If importing from the same package
    .game_round_settings import GameRoundSettings

* the single dot (.) means "this package"

### Module entry points
* if execution of module is done directly, then the value will be _ main _
  * otherwise, it will be the *fully qualified name*
  * ex
    * comission/common/game_enums.py
    * would be
    * omission.common.game_enums

### Package entry points
* if project has a __ main __ in the top level, it will automatically execute when package is executed directly
  * but not when importing the package

### Controlling package imports
* the __ init __.py file can come in handy when you want to chane what is available for import and how it can be used.
* the init file can expose certain subpackages and modules if there happen to be 100's or 1000's of them
* but you can still import other packages to that are outside the init file
* if you can anticipate how a user will interact with your package, you can greatly simplify you code by added a few lines to init

### Program entry point
* to make program start on double click, create a single script file outside the top-level package
* then write:
  > from omission._ main _ import main
  * executing main function 
  > main()