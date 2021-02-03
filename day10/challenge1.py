def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("Leap year.")
                print(True)
                return True
            else:
                print("Not leap year.")
                return False
        else:
            print("Leap year.")
            return True
    else:
        print("Not leap year.")
        return False


def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
    if is_leap(year) and month == 2:
        month_days[1] = 29
        return 29
    else:
        return month_days[month-1]
        print(month_days[month-1])
    
    


    
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)