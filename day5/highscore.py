student_scores = input("Input a list of student heights ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])


highestscore = 0
for score in student_scores:
    if score > highestscore:
        highestscore = score
print(highestscore)

