# collect user height and weight
height = float(input("Please enter your height in meters: "))
weight = float(input("Please enter your weight in Kilograms: "))

# calculate bmi
user_bmi = weight // (height ** 2)

# show user results
print(int(user_bmi))