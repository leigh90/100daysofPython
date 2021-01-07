student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

height_list = 0
counter = 0

for i in student_heights:
    height_list += i 
    counter += 1
print(height_list)
print(counter)

average_height = height_list // counter 
print(average_height)



