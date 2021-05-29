# TODO DICTIONARY COMPREHENSION

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor','Freddie']

# Syntax
# new_dict = { new_key: new_value for item in list}
import random
student_scores = {student: random.randint(1,101) for student in names}
# print(student_scores)
# print(student_scores.items())

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
sentence = sentence.split()
print(sentence)
result = {word:len(word) for word in sentence}
print(result)

# todo Create a new dictionary from an existing dictionary / with conditional
# new_dict = {new_key:new_value for (key,value) in dict.items() if test}
# passed_students = {student:score for student,score in student_scores.items() if score > 50}
# print(passed_students)

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# weather_f = { day:(temp * 9/5 + 32) for (day,temp) in weather_c.items()}
# print(weather_f)
# its the same as doing this
# for key,value in weather_c.items():
#     print(key)
student_dict = {
    "student": ["Angela", " James", "Lilly"],
    "score": [56, 76, 98]
}
import pandas
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

for (index, row) in student_data_frame.iterrows():
    print(row.student)

