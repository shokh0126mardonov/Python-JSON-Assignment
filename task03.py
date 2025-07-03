import json

with open('students.json','r') as jsonfile:
    students_str = jsonfile.read()
    
student = json.loads(students_str)

student_append = {"name": "Shahzoda", "surname": "Nazarova", "age": 22}
student.append(student_append)

student_dump = json.dumps(student,indent = 4)

with open('students.json','w') as jsonfile:
    jsonfile.write(student_dump)