import json
l1=['neelam','programer','24','2400',]
l2=['komal','trainer','24','20000']
l3=['anuradha','HR','25','40000']
l4=['Abhishek','manager','29','63000'] 
dic={}
d={}
p={}
w={}
t={}
i=0
while i<len(l1):
    dic["name"]=l1[0]
    dic["designation"]=l1[1]
    dic["age"]=l1[2]
    dic["salary"]=l1[3]
    i+=1
    j=0
    while j<len(l2):
        w["name"]=l2[0]
        w["designation"]=l2[1]
        w["age"]=l2[2]
        w["salary"]=l2[3]
        j+=1
        k=0
        while k<len(l3):
            t["name"]=l3[0]
            t["designation"]=l3[1]
            t["age"]=l3[2]
            t["salary"]=l3[3]
            k+=1
            q=0
            while q<len(l4):
                p["name"]=l4[0]
                p["designation"]=l3[1]
                p["age"]=l4[2]
                p["salary"]=l4[3]
                q+=1
d["emp1"]=dic
d["emp2"]=w
d["emp3"]=t
d["emp4"]=p
file=json.dumps(d)
print(file)