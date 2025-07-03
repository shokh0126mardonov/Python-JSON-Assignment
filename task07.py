import json

with open('students.json','r') as jsonfile:
    students_str = jsonfile.read()
    students = json.loads(students_str)

sum = 0
for student in students:
    sum += student['age']

overal_age = sum/len(students)
dump_overal = json.dumps(overal_age)
with open('overal_age.json','w') as overal:
    overal.write(dump_overal)