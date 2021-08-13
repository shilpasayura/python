# You can add names here so the program will know them automatically
# when it starts.
namelist = []

print("Options:")
print("  0      Quit")
print("  1      Check if I know you")
print("  2      Introduce yourself to me")
print("  3      Make me forget you")
print("  4      Print a list of people I know")
print()     # print an empty line

while True:
    option = input("Choose an option: ")

    # Things like option == 0 don't work because option is a string
    # and it needs to be compared with a string:
    #   >>> 0 == 0
    #   True
    #   >>> '0' == '0'
    #   True
    #   >>> 0 == '0'
    #   False
    if option == '0':
        print("Bye!")
        break

    elif option == '1':
        name = input("Enter your name: ")
        if name in namelist:
            print("I know you! :D")
        else:
            print("I don't know you :/")

    elif option == '2':
        name = input("Enter your name: ")
        if name in namelist:
            print("I knew you already.")
        else:
            namelist.append(name)
            print("Now I know you!")

    elif option == '3':
        name = input("Enter your name: ")
        if name in namelist:
            namelist.remove(name)
            print("Now I don't know you.")
        else:
            print("I didn't know you to begin with.")

    elif option == '4':
        if namelist == []:
            print("I don't know anybody yet.")
        else:
            for name in namelist:
                print("I know %s!" % name)

    else:
        print("I don't understand :(")

    print()
