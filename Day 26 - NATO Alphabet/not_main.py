import random
# List Comprehension
numbers = [1, 2, 3]
new_list = [n+1 for n in numbers]
print(new_list)
new_list = [n*2 for n in range(1,5)]
print(new_list)
names = ["ishaan", "athena", "pari", "rutvij", "ashmit", "dave"]
short_names = [name for name in names if len(name)<6]
print(short_names)
uppercase_names = [name.upper() for name in names if len(name) > 5]
print(uppercase_names)

# Dictionary Comprehension
names = ["ishaan", "athena", "pari", "rutvij", "ashmit", "dave"]
student_scores = {student : random.randint(1,100) for student in names}
print(student_scores)
passed_students = {student : score for (student, score) in student_scores.items() if score>=60}
print(passed_students)