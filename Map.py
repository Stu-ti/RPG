'''
This is a module that contains a list of all the rooms, as well as nested dictionaries that have the items of the rooms and their descriptions. This 
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
    'closet': {'Description': 'The closet is filled with dirty mops'},
    'office': {'Description': 'There are papers on every corner of the room'},
    'washroom': {'Description': 'The washroom is slippery'},
    'sauna': {'Description': 'The steam is slipping out through the cracks of'
              ' the door'},
    'entrance': {'Description': 'The entrance is locked'},
    'foyer': {'Description': 'There is a large painting in the middle of the'
              ' foyer'},
    'stairs': {'Description': 'The stairs are long and winding'},
    'bedroom1': {'Description': 'The bedroom is table is filled with coffee'
                 ' mugs'},
    'bedroom': {'Description': 'The bedroom smells is filled with the smell of'
                ' jasmine'},
    'washroom1': {'Description': 'The washroom has a large bathtub in the'
                  'middle'},
    'bedroom2': {'Description': 'The bedroom floor is piled with clothes'},
    'theatre': {'Description': 'The theatre has a popcorn machine'},
    'sunroom': {'Description': 'The sunroom seems to be shining, with sunlight'
                ' spilling in'},
    'kitchen': {'Description': 'The kitchen smells like freshly baked bread'},
    'dining': {'Description': 'The dining room has old dark wood furniture'},
    'gym': {'Description': 'The gym as a variety of machines and weights'}
     }

#This is a nested dictionary of all the rooms and the items found in them.
map_items = {
    'closet': {'Item': 'Bleach'},
    'office': {'Item': 'Pen'},
    'washroom': {'Item': 'Lotion'},
    'sauna': {'Item': 'Hot Rock'},
    'entrance': {'Item': 'Slippers'},
    'foyer': {'Item': 'Family Picture'},
    'stairs': {'Item': 'Mat'},
    'bedroom1': {'Item': 'Coffee Mug'},
    'bedroom': {'Item': 'Jasmine Flower'},
    'washroom1': {'Item': 'Toothbrush'},
    'bedroom2': {'Item': 'Book'},
    'theatre': {'Item': 'Popcorn'},
    'sunroom': {'Item': 'Key'},
    'kitchen': {'Item': 'Cupcake'},
    'dining': {'Item': 'Knife'},
    'gym': {'Item': 'Dumbell'}
    }