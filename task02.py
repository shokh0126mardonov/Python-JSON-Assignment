import json

with open('students.json','r') as f1:
    students_str = f1.read()

students = json.loads(students_str)  

for student in students:
    name = student['name']
    age = student['age']
    
    print(f"{name} - {age} yosh")