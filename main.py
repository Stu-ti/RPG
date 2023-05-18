###############################################################################
#Stuti_Home_Adventure
#CS 30
#May 10, 2023
#Stuti Sapru
#Version 004
###############################################################################
'''
A simple game using a map and items in the rooms of the map

The user gets to choose between moving and not moving through a map of an 
house. If they choose not to move, the program stops running. This is
essentially a quit option. If the user wants to move, they can choose between
North, South,  East and West. The program keeps track of the location of the
user and prints it out for them everytime they're faced with the decision to 
move or not again. In every room of the map, there is also an item. This item
is added to the inventory of the user by default. The same item cannot be added
to the user's inventory twice, even if the user goes to the same room more than
one time.
'''

#this calls the module that contains the map, its items and descriptions
import Map
#this calls the module that controls everything related to the user's inventory
import Inventory
#this calls the module that control's the user's movement between rooms and 
#tracks their location
import Movement

#the initial instructions of the game are printed first and do not loop
#throughout the duration of the game
print("Please type all answers exactly as given in the question.\nFor "
      "example, when asked if you want to go North or South, you would "
      "answer 'North' or 'South' only. \n\nHope you enjoy the game! To "
      "stop,type 'Quit'. Below is the map of the house.\n")
#this prints out the text file of the map that the user can view at the 
#start of the game incase of no error
with open("Maps.txt", "r") as file:
    print(file.read())

#this allows the code to loop forver until the user decides to quit and it
#also prints the location of the user with every loop
while Movement.loop == True:
    #this statement prints what room the user is in
    print(f"\nYou are in room: {Map.map[Movement.row][Movement.column]}")
    #this loop prints the description of the room the user is in
    for key in Map.map_rooms:
        if key == Map.map[Movement.row][Movement.column]:
            for des in Map.map_rooms[key]:
                print(f"{Map.map_rooms[key][des]}")
    #this call the function that controls the user's inventory from 
    #another module
    Inventory.get_items()
    #this call the function that controls the user's movement from another 
    #module
    Movement.move()