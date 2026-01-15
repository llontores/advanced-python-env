import json

file = open("students.json", "r")
students = json.load(file)
file.close()

for student in students:
    avg = sum(student["grades"]) / len(student["grades"])
    student["average"] = avg

file = open("students_with_avg.json", "w")
json.dump(students, file, indent=4)
file.close()
