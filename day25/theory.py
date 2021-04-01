import csv
# with open('weather_data.csv') as file:
#     data = file.readlines()
#     print(data)

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

# PANDAS is designed for use with csv files
import pandas as pandas

data = pandas.read_csv('weather_data.csv')
print(data)
print(type(data)) #dataframe
print(data['temp'])
print(type(data['temp'])) #Series

# convert data to dictionary consult documentation for these methods
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data['temp'].to_list()
# print(temp_list)
# average_temp = sum(temp_list) / len(temp_list)
# print(average_temp)
#
# print(data['temp'].mean())
# print(data['temp'].max())
#
# # Get Data in columns
# print(data['condition'])
# print(data.condition)
# # these are the same
#
# # Get Data in Rows
# monday = data[data.day == 'Monday']
# print(data[data.day == 'Monday'])
# print((monday.temp * 9/5) + 32)
# # (0°C × 9/5) + 32
# hottest_temp = data['temp'].max()
# hottest_temp = data.temp.max()
# hottest_day = data[data['temp'] == hottest_temp]
# hottest_day.day
# print(hottest_day)
# print(hottest_day.condition)

# Create a dataframe from scratch
data_dict = {
    'students': ['Amy', 'James', 'Angela'],
    'scores': [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
print(data)

data.to_csv('new_data.csv')







