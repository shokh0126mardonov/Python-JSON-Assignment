import json

with open('students.json','r') as f1:
    students_str = f1.read()

students = json.loads(students_str)

filter_age = list(filter(lambda age: age['age'] > 20,students))

students_dump = json.dumps(filter_age,indent=4)

with open('students.json','w') as f2:
    f2.write(students_dump)