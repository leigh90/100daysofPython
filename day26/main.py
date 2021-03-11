with open('file1.txt') as file1:
    file_one = file1.readlines()

with open('file2.txt') as file2:
    file_two = file2.readlines()


result = [int(num) for num in file_one if num in file_two]
print(result)

