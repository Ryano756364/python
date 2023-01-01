choice = int(input("Please choose your recipe below: \n"
                   "1. Bacon \n"
                   "2. Eggs \n"
                   "3. Apple Pie \n"
                   "4. Toast \n"
                   "0. Quit \n"))

while choice != 0:  # could've also used a True to loop
    if choice == 1:
        print("You chose number {} which is recipe '{}' "
              .format(choice, "1. Bacon"))

    elif choice == 2:
        print("You chose number {} which is recipe '{}' "
              .format(choice, "2. Eggs"))

    elif choice == 3:
        print("You chose number {} which is recipe '{}' "
              .format(choice, "3. Apple Pie"))

    elif choice == 4:
        print("You chose number {} which is recipe '{}' "
              .format(choice, "4. Toast"))

    else:
        # use function instead of repeating menu again
        # or move menu to top of this while loop
        print("Invalid choice, please review menu and try again. \n"
              "1. Bacon \n"
              "2. Eggs \n"
              "3. Apple Pie \n"
              "4. Toast \n"
              "0. Quit \n")

    choice = int(input("Please enter another number on menu \n"))
else:
    print("End of program!")
