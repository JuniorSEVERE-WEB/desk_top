students = [("Junior", 85), ("Senior", 92), ("Sophomore", 78), ("Freshman", 88)]
sorted_students = sorted(students, key = lambda x: x[1])
print(sorted_students)