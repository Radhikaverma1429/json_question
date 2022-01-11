import json
dic={"emp1": {"name": "neelam", "designation": "programer", "age": "24", "salary": "2400"},
    "emp2": {"name": "komal", "designation": "trainer", "age": "24", "salary": "20000"},
    "emp3": {"name": "anuradha", "designation": "HR", "age": "25", "salary": "40000"}}
with open("w3resource6.json","w") as f:
    data=json.dump(dic,f,indent=4)

