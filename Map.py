'''
This is a module that contains a list of all the rooms, as well as nested
dictionaries that have the items of the rooms and their descriptions. This 
module is used to track the location of the user in respect to their position 
on the map.
'''
#this helps format the map when it is written to
from tabulate import tabulate

#This is a list of all the rooms
map = [['closet', 'office', 'washroom', 'sauna'],
       ['entrance', 'foyer', 'stairs', 'bedroom1'],
       ['bedroom', 'washroom1', 'bedroom2', 'theatre'],
       ['sunroom', 'kitchen', 'dining', 'gym']]

#This is a nested dictionary of all the rooms and the their dictionaries.
map_rooms = {
  'closet': {
    'Description': 'The closet is filled with dirty mops'
  },
  'office': {
    'Description': 'There are papers on every corner of the room'
  },
  'washroom': {
    'Description': 'The washroom is slippery'
  },
  'sauna': {
    'Description': 'The steam is slipping out through the cracks of'
    ' the door'
  },
  'entrance': {
    'Description': 'The entrance is locked'
  },
  'foyer': {
    'Description': 'There is a large painting in the middle of the'
    ' foyer'
  },
  'stairs': {
    'Description': 'The stairs are long and winding'
  },
  'bedroom1': {
    'Description': 'The bedroom is table is filled with coffee'
    ' mugs'
  },
  'bedroom': {
    'Description': 'The bedroom smells is filled with the smell of'
    ' jasmine'
  },
  'washroom1': {
    'Description': 'The washroom has a large bathtub in the'
    'middle'
  },
  'bedroom2': {
    'Description': 'The bedroom floor is piled with clothes'
  },
  'theatre': {
    'Description': 'The theatre has a popcorn machine'
  },
  'sunroom': {
    'Description':
    'The sunroom seems to be shining, with sunlight'
    ' spilling in'
  },
  'kitchen': {
    'Description': 'The kitchen smells like freshly baked bread'
  },
  'dining': {
    'Description': 'The dining room has old dark wood furniture'
  },
  'gym': {
    'Description': 'The gym as a variety of machines and weights'
  }
}

#This is a nested dictionary of all the rooms and the items found in them.
map_items = {
  'closet': {
    'Item': 'Bleach'
  },
  'office': {
    'Item': 'Pen'
  },
  'washroom': {
    'Item': 'Lotion'
  },
  'sauna': {
    'Item': 'Hot Rock'
  },
  'entrance': {
    'Item': 'Hot Rock'
  },
  'foyer': {
    'Item': 'Family Picture'
  },
  'stairs': {
    'Item': 'Mat'
  },
  'bedroom1': {
    'Item': 'Coffee Mug'
  },
  'bedroom': {
    'Item': 'Jasmine Flower'
  },
  'washroom1': {
    'Item': 'Toothbrush'
  },
  'bedroom2': {
    'Item': 'Book'
  },
  'theatre': {
    'Item': 'Popcorn'
  },
  'sunroom': {
    'Item': 'Key'
  },
  'kitchen': {
    'Item': 'Cupcake'
  },
  'dining': {
    'Item': 'Knife'
  },
  'gym': {
    'Item': 'Dumbell'
  }
}


def question():
    #this asks the user if they want to see the map
    ask = input("Do you want to see the map? ")

    if ask == "Yes":
        #this asks if the user is ready to accept conditions (extra layer of user input)
        add = input("Are you ready to accept all the information that comes with looking at the map? ")
        #if the user decides that they want to see the map and accept all terms and 
        #conditions
        if add == "Yes":
            #runs if there is nopthing wrong with the code
            try:
                #writes the map to an external file
                with open("Maps.txt", "w") as file:
                    file.write(tabulate(map, tablefmt="grid"))
            #The statement below prints if there is an error in printing the
            #module that contains the text version of the map
            except:
                print("There is no available map of the house right now. Please "
                      "contact the game developer and let them know. You will have"
                      " to play the game without a map. Apologies for the "
                      "inconvinience.")
            #this is further printed if the code does not have an error
            else:
                with open("Maps.txt", "r") as file:
                    print(file.read())
            #this prints no matter if something is wrong with the file or not
            finally:
                print("You can view it later in the game as well!")
        #this prints if the user does not accept the terms and conditions
        elif add == "No":
            print("\nOkay! You can choose to view it later!")
        #the following statement prints if the user types an invalid input
        else:
            print("\nPlease print out either 'Yes' or 'No' only!")
            question()
    #the statement below prints out incase the user does not want to see the map
    elif ask == "No":
        print("\nYou can choose to view the map later in the game!")
    #the following statement prints if the user types an invalid input
    else:
        print("\nPlease print out either 'Yes' or 'No' only!")
        question()