import random
import pandas

""" List Comprehension """
numbers = [1, 2, 3, 4]
new_list = [number + 1 for number in numbers]
print(new_list)

name = "Tantowi"
char_list = [char for char in name]
print(char_list)

names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
long_names  = [name.upper() for name in names if len(name) > 5]

print(short_names, long_names)

""" Dictionary Comprehension """
students_score = {name:random.randint(0, 100) for name in names}
print(students_score)

passed_students = {name:score for(name, score) in students_score.items() if score >= 60}
print(passed_students)

""" Loop Through Pandas DataFrame """
student_data = {
    "name": ["Test1", "Test2", "Test3"],
    "score": [60, 70, 80]
}

""" Loop through columns """
student_data_frame = pandas.DataFrame(student_data)
for (name, score) in student_data_frame.items():
    print(name)

""" Loop through rows Using iterrows """
for (index, row) in student_data_frame.iterrows():
    print(index, row)

""" Loop through rows Using itertuples """
for (index, name, score) in student_data_frame.itertuples():
    print(index, name, score)
