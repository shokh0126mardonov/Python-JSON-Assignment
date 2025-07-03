import json

with open('students.json','r') as f1:
    students = json.loads(f1.read())
    
    growth_age = sorted(students,key=lambda age:age['age'])
    
with open('grow_age.json','w') as f2:
    f2.write(json.dumps(growth_age,indent=4))
    