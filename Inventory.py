'''
This is a module that controls the user's inventory. If the user moves into a 
certain room, this module contains a function that prints out what item they 
found in that room and adds it to their inventory. It also lets the user know 
if they already had that particular item in their inventory. If they did, the 
item is not added to their inventory again. Laastly, it prints out all the 
items the user had in their inventory.
'''
#this calls the module that contains the map, its items and descriptions
import Map
#this calls the module that controls the user's movement and tracks their 
#location
import Movement
#this variable is an empty list that will hold the items collected in each room
inventory = []


def get_items():
    """
    This is a funtion that allows the user to view what items they have in 
    their inventory. Additionally, every time the user reachs a certain room,
    the function adds the items of the corresponding room to the inventory. If
    the user reaches a certain room twice, the item of the corresponding room
    is not readded to the inventory.
    """
    #this line of code calls the variable we defined previously
    global inventory
    #this loop prints the item of the room the user went into
    for room in Map.map_items:
        if room == Map.map[Movement.row][Movement.column]:
            for item in Map.map_items[room]:
                print(f"\nYou found {Map.map_items[room][item]}\n")
                #this loop adds the item to the user's inventory. If the
                #inventory already has the item, the item is not readded.
                if Map.map_items[room][item] in inventory:
                    print("You already have this in your inventory\n")
                else:
                    inventory.append(Map.map_items[room][item])
    #this loop prints all the items of the inventory for the user. If the user 
    #has no items in their inventory, the loop prints the same to let the user 
    #know
    if len(inventory) != 0:
        for i in inventory:
            print(f"You have: - {i}")
    elif len(inventory) == 0:
        print("Your inventory is empty.\n")