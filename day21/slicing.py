piano_keys = ["a","b","c","d","e","f","g"]
# slice: to cut a part of a list and return that part of the list
print(piano_keys[2:5])
# >>>['c', 'd', 'e']
# this notation indicates the start point and up to but not including the elemnt at the last index
# in this case slice from index 2 to before index 5 so it will grab index 2,3 and 4

# from beginning to before indicated index
print(piano_keys[:5])
# >>>['a', 'b', 'c', 'd', 'e']

# you can add an increment level
# give me from 2 to before 5 every 2 elements
print(piano_keys[2:5:2])
# >>>['c', 'e']

# give all elements skip the second element
print(piano_keys[::2])
# >>>['a', 'c', 'e', 'g']
# note that it will start with the first element and start counting the step from there.
print(piano_keys[::-1])
# >>>['g', 'f', 'e', 'd', 'c', 'b', 'a']
# cool trick to reverse a list because it returns the elements from the last element in the list
# SLICING TUPLES same as list
piano_tuple=("do","re","me","fa","so","la","ti","do")
print(piano_tuple[1])






