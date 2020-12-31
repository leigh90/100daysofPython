print('Welcome to The Coder\'s Pizzeria')
pizza_size = input("What size pizza do you want? S, M or L").upper()
add_pepperoni = input("Do you want Pepperoni? Y or N").upper()
extra_cheese = input('Do you want extra cheese? Y or N').upper()
price = 0

if pizza_size == 'S':
    price = 100
    if add_pepperoni == 'Y':
        price += 50
        print(price)
elif pizza_size == 'M':
    price = 200
    if add_pepperoni == 'Y':
        price += 50
        print(price)
else:
    price = 300
    if add_pepperoni == 'Y':
        price += 50
        print(price)
if extra_cheese == 'Y':
    price += 1

print(f'You will pay Ksh{price}')

