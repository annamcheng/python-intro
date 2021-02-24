# ###############################
# # DATA TYPES
# ###############################
# # integers (int) = whole numbers (3, 300)
# # floating point (float) = numbers with decimal points (1.5, 10.0)
# # Booleans (bool) = logical value indictating True or False
# # strings(str) = ordered seq of chars//IMMUTABLE ("Hello", "Anna")
# # Lists (list) = ordered seq of objs//MUTABLE [123,'hello',true]
# # Tuples (tup) = ordered seq of objs//IMMUTABLE (123, 'hello', true, true)
# # Dictionaries (dict) = unordered key-value pairs//MUTABLE{"first_name":"Anna", "last_name":"Cheng"}
# # Sets (set) = unodered and unindexed collection of unique objs {"a", "b"}
# # Frozen set () = 

# ###############################
# # STRING 
# ###############################
# # Strings are ordered and immutable sequence of characters
# # FORMATTING with .format()
# # Syntax: "String here {}".format("insert string")
# print("Coding in {1} {0} {2}".format("is", "Python", "fun"))
# print("Coding in {p} {i} {f}".format(i="is", p="Python", f="fun"))

# # f-string (Introduced in Python 3.6) AKA Literal String
# adjective= "fun"
# print(f"Coding in Python is {adjective}")
# # Output for all of the above: Coding in Python is fun

# # More practice/examples with .format()
# name = "Bob"
# age = 30
# print("His name is {0} and he is {1} years old.".format(name, age))
# # His name is Bob and he is 30 years old.

# myorder = "May {person} please have a {foodname} with a side of {side}"
# print(myorder.format(foodname="cheeseburger", side="fries", person="Julie"))
# # May Julie please have a cheeseburger with a side of fries.

# # FLOAT FORMATTING
# # Syntax: "{value:width.precision f}"
# result = 100 / 777
# print("The result is {r:1.3f}".format(r=result))
# # The result is 0.129

# price = 15
# txt = "The price is {:.2f} dollars"
# print(txt.format(price))
# # The result is 15.00 dollars

# # SLICING STRINGS
# # Syntax: [start:stop:step]
# # start = numerical index for where you want to start
# # stop = index to go up to but NOT including
# # step = size of steps you want to take

# # start at the index of 1; stop at the index of 5 but not including
# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# print(alphabet[1:5]) # bcde

# # print out every other letter starting from f to the end, which is at the index of 5
# print(alphabet[5::2]) # fhjlnprtvxz

# ###############################
# # LIST
# ###############################
# # ordered & mutable sequence of objects within square brackets
# # NOTE: Unlike Strings, Lists are mutable!
# # NOTE: Ordered Sequence can be indexed or sliced

# my_avengers_list = ['Captain America', 'Black Widow', 'Iron Man']
# my_avengers_list_2 = ['Hawk Eye', 'Scarlet Witch', 'Vision']

# # slice the list starting from the index of 1
# # result: ['Black Widow', 'Iron Man']
# print(my_avengers_list[1:])

# # mutate the list by permanently renaming Iron Man to Tony Stark at the index of 2
# my_avengers_list[2] = 'Tony Stark'
# print(my_avengers_list)

# # You can append two lists together saved in a new variable
# new_list = my_avengers_list + my_avengers_list_2
# print(new_list)


# # METHODS
# # use append() method to add the end of the list
# # add Thor to end of new_list
# new_list.append('Thor')
# print(new_list)

# # use  pop() method to remove at the end of the list
# # remove Vision from the end of new_list
# new_list.pop()
# print(new_list)

# # indicate which element you want to remove by their index
# # remove Captain America from new_list at index 0
# new_list.pop(0)
# print(new_list)

# # sort() can sort strings and numbers
# # happens in place, must run on the variable itself and not within new variable
# letters = ['x', 'b', 't', 'g']
# numbers = [5, 9, 3, 1]

# letters.sort()
# numbers.sort()
# print(letters) # ['b', 'g', 't', 'x']
# print(numbers)  # [1, 3, 5, 9]

# # reverse() reorders list in descending order
# letters.reverse()
# numbers.reverse()
# print(letters) # ['b', 'g', 't', 'x']
# print(numbers)  # [1, 3, 5, 9]

# # ###############################
# # # DICTIONARIES
# # ###############################
# # unordered mappings for storing objects using key-value pairings and are mutable
# # can easily grab objects without needing to know an index location
# # NOTE: Unordered and cannot be sorted. Objects retreived by key name.
# # If you want dictionary capability AND ordering, use ordereddict

# # print out flavor of icecream
# icecream_dict = {"flavors": ["vanilla", "strawberry", "rocky road"], "price": "3.50"}
# print(icecream_dict['flavors'])  # ['vanilla', 'strawberry', 'rocky road']

# # dictionaries are flexible and can chain commands calls to mutate key-value pairs
# print(icecream_dict['flavors'][1].upper()) # STRAWBERRY
# icecream_dict['flavors'].append('chocolate')
# print(icecream_dict) # {'flavors': ['vanilla', 'strawberry', 'rocky road', 'chocolate']}

# # add more key-value pairs to the dictionary
# icecream_dict['cup or cone'] = 'cone'
# print(icecream_dict)
# # {'flavors': ['vanilla', 'strawberry', 'rocky road', 'chocolate'], 'price': '3.50', 'cup or cone': 'cone'}

# # can override existing key-value pairs
# icecream_dict['flavors'] = ['rhubarb', 'green tea', 'sesame']
# print(icecream_dict)
# # {'flavors': ['rhubarb', 'green tea', 'sesame'], 'price': '3.50', 'cup or cone': 'cone'}

# # METHODS
# # .keys() will return all keys
# # .values () will return all values
# # .items() will return key-value pairs
# print(icecream_dict.keys()) # (['flavors', 'price', 'cup or cone'])
# print(icecream_dict.values()) # ([['rhubarb', 'green tea', 'sesame'], '3.50', 'cone'])
# print(icecream_dict.items())  # ([('flavors', ['rhubarb', 'green tea', 'sesame']), ('price', '3.50'), ('cup or cone', 'cone')])

# ###############################
# # TUPLES
# ###############################
# similar to lists, however, IMMUTABLE
# once inside a tuple, elements cannot be reassigned.
mylist = (1, 2, 'hello')

# ONLY HAS TWO BUILT IN METHODS
# COUNT // count() takes exactly one argument
# See how many times a shows up in tuple
t = ('a', 'a', 'b')
print(t.count('a'))  # 2

# INDEX // index() takes exactly one argument
# See which index the argument first appears
print(t.index('a'))  # index 0

# ###############################
# # SETS
# ###############################
# Unordered collections of unique elements
# There can only be one represeentative of the same obj
# If you have a list of numbers, set will only return one of each unique element
list_of_numbers = [1, 1, 1, 2, 2, 2, 3, 3, 3]
print(set(list_of_numbers))  # {1,2,3}
#method
# .add() to add to set

# Comparison operators
# We can use logical operators to combine comparisons: and / or / not
# AND: both conditionals has to be true
print(('h' == 'h') and (2 == 2))  # true
# OR: only one condition has to be true
print((1 == 100) or (2 == 2))  # true
# NOT: return opposite boolean
print(not 1 == 1)  # was true but not keyword makes it false

