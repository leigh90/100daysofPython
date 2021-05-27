# Error Catching
# try: Something that might cause an Exception (this may or may not work)
# except: do this if there was an exception 
# else: do this if there were no exceptions
# finally: do this no matter what happens, this block is always executed
# a_dictionary = {"Key":"value"}
# # print(a_dictionary["sdsfds"])

# try:
#     file= open('a_file.txt')
#     a_dictionary = {"Key":"value"}
#     print(a_dictionary["sdsfds"])
# except FileNotFoundError:
#     file = open("a_file", "w")
#     file.write('Telly')
# except KeyError as error_message:
#     print(f"The Key {error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("File was closed.")
#     raise KeyError
#     raise TypeError("I'm making this up as I go")

# TODO RAISING ERRORS

height = float(input('Height: '))
weight = int(input('Weight: '))

if height > 3:
    raise ValueError("Human Heights shouldnt be over 3 meters")

    

bmi = weight /height ** 2
print(bmi)