import json

with open('students.json','r') as f1:
    students = json.loads(f1.read())
    max_age = max(students,key=lambda age: age['age'])
    
    max_dump = json.dumps(max_age)

with open('max_age.json','w') as f2:
    f2.write(max_dump)