
# with open('weather_data.csv') as file:
#     data = file.readlines()
#     print(data)

import csv
# import pandas
import pandas as pandas

data = pandas.read_csv('weather_data.csv')
print(data)
print(data['temp'])

# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     print(data)
#     temperatures = []
#     new_list = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     temperatures.pop(0)
#     print(temperatures)



