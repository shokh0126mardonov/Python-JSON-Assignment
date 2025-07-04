import json
import os

filename = 'students.json'

if not os.exists(filename):
    with open('filename','w') as f1:
        json.dump([], f1 , indent=4)
        print(f"{filename} yaratildi.")
else:
    print(f"{filename} avjud ekan.")
    
