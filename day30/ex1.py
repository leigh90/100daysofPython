fruits = ["Apple", "Pear", "Orange"]
index = int(input('Enter a number between 0 and 3: '))

#TODO: Catch the exception and make sure the code runs without crashing.

def make_pie(index):
    
    try:
        fruit = fruits[index]
    except IndexError:
        print('Fruit Pie')
    else:
        print(fruit + " pie")

    

    
make_pie(index)