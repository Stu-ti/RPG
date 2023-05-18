'''
This is a module that controls the user's movement throughout the game. It 
allows the user to choose if they want to move or not, as well as if they 
want to move north, south, east or west on the map. They can also quit the 
game at any time by tying the word 'Quit'.
'''
#this calls the module that contains the global variables used across modules
#this variable determines whether the code should continue forever or break
#off
loop = True
#this indicates the room the user is initially in on a horizontal plane
row = 3
#this variable indicates the room the user is initially in on a vertical plane
column = 0


def move():
    """
    This function allows the user to choose whether they want to move or to
    quit the game. It continues forever until the user chooses to quit the
    game. If the user chooses to move, this function also allows them to
    choose the direction they want to move in.
    """
    #the variables we defined above are called in this function
    global row, column, loop
    #this allows the user to choose between moving or quitting
    walk = input("\nDo you want to move or not? Your options are Yes or No. ")

    #if the user chooses to not move, the game stops
    if walk == "No":
        loop = False

    #if the user chooses to quit, the game stops
    elif walk == "Quit":
        loop = False

    #if the user chooses to move, the game proceeds
    elif walk == "Yes":
        #the user can move North, South, East or West of the default room
        print("\nGood choice! You can move North, South, East or West.")
        direction = input("Where would you like to go? ")

        #the user chooses to move North and they move in a room in the row
        #above
        if direction == "North":
            if row > 0:
                row -= 1

            elif row == 0:
                print("\nYou're at the edge of the map. Please choose another "
                      "direction")

        #the user chooses to move South and they move in a room in the row
        #below
        elif direction == "South":
            if row < 3:
                row += 1

            elif row == 3:
                print("\nYou're at the edge of the map. Please choose another "
                      "direction")

        #the user chooses to move East and they move in a room in the
        #column to the right
        elif direction == "East":
            if column < 3:
                column += 1

            elif column == 3:
                print("\nYou're at the edge of the map. Please choose another "
                      "direction")

        #the user chooses to move North and they move in a room in the
        #column to the left
        elif direction == "West":
            if column > 0:
                column -= 1

            elif column == 0:
                print("\nYou're at the edge of the map. Please choose another "
                      "direction")

        #if the user chooses to quit the game, the game stops
        elif direction == "Quit":
            loop = False

        #the following statement prints if the user types an invalid input
        else:
            print("\nI  didn't understand that. Please try again.")

    #if the user chooses to quit, the game stops
    elif walk == "Quit":
        loop = False

    #the following statement prints if the user types an invalid input
    else:
        print("\nI didn't understand that. Please try again.")