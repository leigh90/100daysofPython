import pandas as pandas

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
# print(data)

fur_color = data['Primary Fur Color']
print(fur_color)

grey = data[data['Primary Fur Color'] == 'Gray']
print(type(grey))
grey_no = len(grey)
print(grey_no)

cinnamon = data[data['Primary Fur Color'] == 'Cinnamon']
cinnamon_no = len(cinnamon)
print(cinnamon_no)

black = data[data['Primary Fur Color'] == 'Black']
black_no = len(black)
print(black_no)


squirrel_data = {
    'Fur color': ['Gray', 'Cinnamon', 'Black'],
    'Count': [2473, 392, 103]
}

data = pandas.DataFrame(squirrel_data)
data.to_csv('squirrel_data.csv')
