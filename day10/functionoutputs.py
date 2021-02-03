# def my_function():
#     result = 3 * 20
#     return result


# output = my_function() #output will store the result of the function 3 * 20 so output will be 60
# print(output)

# def format_name(f_name, l_name):
#     proper_name = f_name.title() + " " + l_name.title()
#     return proper_name

# full_name = format_name('ashley', 'zawadi')
# print(full_name)

# MULTIPLE RETURN VALUES
# return marks the end of a function

def format_name(f_name, l_name):
    """
    The funtion takes the first and last name and formats it to title case
    """
    if f_name == "" or l_name == "":
        return "You must provide valid inputs"
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"Your name is {formatted_f_name} {formatted_l_name}"

print(format_name('aSHLEy', "xawadi"))