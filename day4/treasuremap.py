row1 = ['⬜️', '⬜️', '⬜️']
row2 = ['⬜️', '⬜️', '⬜️']
row3 = ['⬜️', '⬜️', '⬜️']

mape = [row1, row2, row3]
print(f'{row1}\n{row2}\n{row3}')

# fetch user input
position_number = input('Enter two numbers from 1 to 3 each followed by a comma')

# get the index positions
position_list = []
new_position_list = position_number.split(',')
number1 = int(new_position_list[0]) -1
number2 = int(new_position_list[1]) -1
position_list.append(number1)
position_list.append(number2)

print(number1,number2)
print(position_list)

column = position_list[0]
row = position_list[1] 
maposition = [column, row]

# put the treasure
mape[column][row] = 'X'
print(mape)





# x_position = 