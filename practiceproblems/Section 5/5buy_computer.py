current_choice = "-"
computer_parts = []  # create an empty list, list to store items

while current_choice != '0':
    if current_choice in "123456":
        print("Adding {}".format(current_choice))
        if current_choice == '1':
            computer_parts.append("computer")
        elif current_choice == '2':
            computer_parts.append("monitor")
        elif current_choice == '3':
            computer_parts.append("keyboard")
        elif current_choice == '4':
            computer_parts.append("mouse")
        elif current_choice == '5':
            computer_parts.append("mouse mat")
        elif current_choice == '6':
            computer_parts.append("hdmi cable")
    else:
        print("Please add options from the list below:")
        print("1: Computer")
        print("2: Monitor")
        print("3: Keyboard")
        print("4: Mouse")
        print("5: Mouse Mat")
        print("6: HDMI Cable")
        print("0: to finish")

    current_choice = input()

print(computer_parts)

# menu structure | input
