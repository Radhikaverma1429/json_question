# Write a Python program to convert Python dictionary object (sort by key)
# to JSON data. Print the object members with indent level 4.

import json
dic={'4': 5,'6': 7,'1': 3,'2': 4}
f=json.dumps(dic,indent=4,sort_keys=True)
print(f)

