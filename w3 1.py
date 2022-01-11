# Write a Python program to convert JSON data to Python object. 

import json
dic='{"name": "David","class":"I","age": 6}'
f=json.loads(dic)
print(f) 