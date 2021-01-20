student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}
#TODO-2: Write your code below to add the grades to student_grades.👇
for score in student_scores:
    if student_scores[score] >= 91:
        print(student_scores[score])
        student_grades[score]='Outstanding'
    elif student_scores[score] >= 81:
        print(student_scores[score])
        student_grades[score]='Exceeds expectation'
    elif student_scores[score] >= 71:
        print(student_scores[score])
        student_grades[score]='Acceptable'
    else:
        print(student_scores[score])
        student_grades[score]='Fail'
    

# 🚨 Don't change the code below 👇
print(student_grades)