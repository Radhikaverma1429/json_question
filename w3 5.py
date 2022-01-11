#Write a Python program to convert JSON encoded data into Python objects

import json
from os import pathconf
python_dict =  {"name": "David", "age": 6, "class":"I"}
python_list =  ["Red", "Green", "Black"]
a=json.dumps(python_dict)
b=json.dumps(python_list)
print(a)
print(b) 