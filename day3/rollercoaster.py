print("Welcome to RollerCoatster")
height = int(input("How tall are you in cm: "))
# age = int(input("How old are you: "))
bill = 0

if height > 120:
    print("Yay you can ride the rollercoaster")
    age = int(input("How old are you: "))

    if age < 12:
        bill = 50
        print("Children pay Ksh 50")
    elif age < 18:
        bill = 120
        print("Teens pay Ksh120")
    elif age >= 45 and age <= 55:
        bill = 0
        print("Everything is going to be fine, have a free ride on us!")
    else:
        bill = 180
        print("Please pay Ksh180")

    want_photos = input("Do you want pictures taken Y or N ").upper()
    if want_photos == "Y":
        bill += 30 #same as bill = bill + 30
    print (f"Your bill is Ksh{bill}")
else:
    print("Sorry love you can't ride today")