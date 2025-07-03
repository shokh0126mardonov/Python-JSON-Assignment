import json

students = [
    {"name": "Ali", "surname": "Valiyev", "age": 20},
    {"name": "Laylo", "surname": "Karimova", "age": 21},
    {"name": "Bekzod", "surname": "Xolmatov", "age": 19}
]

json_dumps = json.dumps(students,indent=4)

with open('students.json','w') as f1:
    f1.write(json_dumps)