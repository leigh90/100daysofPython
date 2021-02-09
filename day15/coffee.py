from menu import MENU, resources
make_order = True
# TODO 1. Money and conversions
# penny = 1ct (1/one_dollar)
one_dollar = 100.0
penny = 1/one_dollar
# print(penny)
# dime = 10cts (10/one_dollar)
dime = 10/one_dollar
# print(dime)
# nickel = 5cts (5/one_dollar)
nickel = 5/one_dollar
# print(nickel)
# 1 qtr = 25cts (25/one_dollar)
qtr = 25/one_dollar
# print(qtr)
# TODO 2. Drink Selection and Prices
# espresso = one_dollar * 1.5
espresso = MENU['espresso']
# print(espresso)
# espresso_price = espresso['cost']
# print(espresso_price)
# espresso_ingredients = espresso['ingredients']
# print(espresso_ingredients)
latte = MENU['latte']
cappuccino = MENU['cappuccino']
drinks_list = [espresso, latte, cappuccino]
# latte = one_dollar * 2.5
# cappuccino = one_dollar * 3.0
# TODO 5. Print a status report of current resources
water = resources['water']
# print(water)
milk = resources['milk']
# print(milk)
coffee = resources['coffee']
# print(coffee)
resource_list = [water, milk, coffee]
# def manage_resources(order):


# TODO 7. Check if Resources are enough
def report(drink, resources):
    print(f" Coffee: {resources['coffee']}gm")
    print(f" Water: {resources['water']}ml")
    print(f" Milk: {resources['water']}ml")


# TODO 8. Make a drink
def make_drink(drink):
    print(drink['ingredients'])
    print(drink['ingredients']['water'])
    print(drink['ingredients']['water'])
    # account for drinks with no milk
    if 'milk' in drink:
        resources['milk'] -= drink['ingredients']['milk']
        # print(resources['milk'])
        resources['water'] -= drink['ingredients']['water']
        # print(resources['water'])
        resources['coffee'] -= drink['ingredients']['coffee']
        # print(resources['coffee'])
        return resources
    else:
        resources['water'] -= drink['ingredients']['water']
        # print(resources['water'])
        resources['coffee'] -= drink['ingredients']['coffee']
        # print(resources['coffee'])
        report(drink, resources)
        return resources


# TODO 3. MAKE A PAYMENT
def pay(drink):
    qtr_pay = int(input("How many quarters? "))
    dime_pay = int(input("How many dimes? "))
    nickel_pay = int(input(" How many nickels? "))
    penny_pay = int(input("How many pennies? "))
    payment_given = (qtr_pay * qtr) + (dime_pay * dime) + (nickel_pay * nickel) + (penny_pay * penny)
    print(payment_given)
    if payment_given >= drink['cost']:
        balance = payment_given - drink['cost']
        print(f"Here is your USD{balance} back. ")
        print(f"Here is your {drink_choice} == Enjoy")
        make_drink(drink)
    elif payment_given < drink['cost']:
        print("Sorry that's not enough")


# TODO 6. Order a drink
# TODO 9.CHECK IF YOU HAVE ENOUGH FOR DRINKS
while make_order:
    drink_choice = input("What would you like?(espresso/latte/cappuccino): ").lower()
    if drink_choice == 'espresso':
        drink = drinks_list[0]
        # print(drink['cost'])
        print(drink['ingredients']['water'])
        if resources['water'] > drink['ingredients']['water'] and resources['coffee'] > drink['ingredients']['coffee']:
            print(f"An Espresso is ${espresso['cost']}")
            pay(drink)
        else:
            print('Sorry we cannot fulfill your request')
            make_order = False
    elif drink_choice == 'latte':
        drink = drinks_list[1]
        # print(drink['cost'])
        if resources['water'] > drink['ingredients']['water'] and resources['coffee'] > drink['ingredients']['coffee'] and \
                resources['milk'] > drink['ingredients']['milk']:
            print(f"A Latte is ${latte['cost']}")
            pay(drink)
        else:
            print('Sorry we cannot fulfill your request')
            make_order = False
    elif drink_choice == 'cappuccino':
        drink = drinks_list[1]
        # print(drink['cost'])
        if resources['water'] > drink['ingredients']['water'] and resources['coffee'] > drink['ingredients']['coffee'] and \
                resources['milk'] > drink['ingredients']['milk']:
            print(f"An Cappuccino is ${cappuccino['cost']}")
            pay(drink)
        else:
            print('Sorry we cannot fulfill your request')
            make_order = False
    else:
        print(" Please select one of the drinks provided ")
