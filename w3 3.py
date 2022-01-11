# Write a Python program to convert Python objects into JSON strings. Print all the values.

import json
from os import pathconf
python_dict =  {"name": "David", "age": 6, "class":"I"}
python_list =  ["Red", "Green", "Black"]
python_str =  "Python Json"
python_int =  (1234)
python_float =  (21.34)
python_T =  (True)
python_F =  (False)
python_N =  (None) 
a=json.dumps(python_dict)
b=json.dumps(python_list)
c=json.dumps(python_str)
d=json.dumps(python_int)
f=json.dumps(python_float)
g=json.dumps(python_T)
h=json.dumps(python_F)
i=json.dumps(python_N)
print(a)
print(b)
print(c)
print(d)
print(f)
print(g)
print(h)
print(i)