import json

with open('students.json','r') as f1:
    students = json.loads(f1.read())
total_student = len(students)    

total_student_dict = {'Umumiy talabalar : ',total_student}

dump_students = json.dumps(list(total_student_dict),indent=4)
 
with open('total_student.json','w') as f2:   
    f2.write(f"{dump_students}")