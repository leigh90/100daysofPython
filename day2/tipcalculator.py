print("Welcome to the Tip Calcultar")
bill = float(input("How much is the total bill? Ksh"))
tip = float(input("What percentage tip do you want to give? 10,12,15 or 18: "))
num_of_people = int(input("How many people are splitting the bill? "))


tip_in_decimal =  ((100 + tip) / 100 )
print(tip_in_decimal)
total_bill = (bill * tip_in_decimal) / num_of_people
print(round(total_bill, 2))