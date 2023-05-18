'''
This is a module that contains a list of all the rooms, as well as nested
dictionaries that have the items of the rooms and their descriptions. This 
module is used to track the location of the user in respect to their position 
on the map.
'''
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
    'Item': 'Slippers'
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
        #this prints out the text file of the map that the user can view at 
        #the start of the game incase of no error
        try:
            with open("Maps.txt", "r") as file:
                print(file.read())
        except:
            #The statement below prints if there is an error in printing the 
            #module that contains the text version of the map
            print("There is no available map of the house right now. Please "
                  "contact the game developer and let them know. You will have"
                  " to play the game without a map. Apologies for the "
                  "inconvinience.")
        else:
            print("\nAbove is the map of the house.")
        finally:
            print("It's just a house!")
    elif ask == "No":
        print("You can choose to view the map later in the game!")
    else:
        print("Please print out either 'Yes' or 'No' only!\n")
        question()
