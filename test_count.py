#!/usr/bin/python3

from models import storage
from models.place import Place
from models.review import Review
from models.city import City
from models.state import State
from models.user import User
from models.amenity import Amenity

ls = []
obj_lis = [Amenity, City, Place, Review, State, User]
all_obj = storage.all(State)
dict = {}
for i, v in all_obj.items():
    dict['__class__'] = v.__class__.__name__
    dict['created_at'] = v.created_at
    dict['id'] = v.id
    dict['name'] = v.name
    dict['updated_at'] = v.updated_at
    ls.append(dict)
#print(ls)

fr = []
for key in all_obj.values():
    stated = key.to_dict()
    fr.append(stated)
#print(f"FR {fr}")


new = State()
name = {'name': 'Carlifornia'}
for u, o in name.items():
    setattr(new, u, o)
print(new)
