# collect user height and weight
height = float(input("Please enter your height in meters: "))
weight = float(input("Please enter your weight in Kilograms: "))

# calculate bmi
user_bmi = weight // (height ** 2)
int(user_bmi)

# show user results
print(user_bmi)

if user_bmi < 18:
    print(f'Your bmi is {user_bmi} and are considered underweight')
elif user_bmi >= 18 and user_bmi < 25:
    print(f'Your bmi is {user_bmi} and are considered to have a normal weight')
elif user_bmi >= 25 and user_bmi < 30:
    print(f'Your bmi is {user_bmi} and are considered overweight')
elif user_bmi >= 30 and user_bmi < 35:
    print(f'Your bmi is {user_bmi} and are considered obese') 
else:
    print (f'Your bmi is {user_bmi} and are considered clinically obese')