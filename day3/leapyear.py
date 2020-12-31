year = int(input('Which year do you '))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print('Leap Year')
        else:
            print('Not a Leap year')
    else:
        print('Leap Year')
else:
    print('Not a leap year')
