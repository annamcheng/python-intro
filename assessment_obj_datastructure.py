# Data structure = used to store a collection of reelated data
# There are 4 built-in data structures in Python: list, tuple, dictionary and set
# Numbers store numerical information and comes in two forms: integers which are whole numbers or floating points which are numbers with decimal points
# Strings are an ordered sequence of characters, immutable, within quotation marks
# Lists are ordered sequence of objects, can be duplicated, mutable, within square brackets
# Tuples are ordered sequence of objects, can be duplicated, immutable, within parens
# Dictionaries are unordered mappings of key-value pairs, cannot be duplicated, within curly brackets
num = 5 ** 3 + 0.25 / 1 - 25
print(num)

# Answer these 3 questions without typing code. Then type code to check your answer.
# PEMDAS
# What is the value of the expression 4 * (6 + 5)
# 11 * 4 = 44
# What is the value of the expression 4 * 6 + 5 
# 24 + 5 = 29
# What is the value of the expression 4 + 6 * 5 
# 30 + 4 = 34

# What is the type of the result of the expression 3 + 1.5 + 4?
# 8.5 is a floating point

# What would you use to find a number’s square root, as well as its square?
# A SQUARE is the result of a number multiplied by itself
# 10 ** 2 #100

# SQUARE ROOT of a number is a value that when multiplied by itself, gives the number. (Sqrt of 16 is 4)
# 100 ** 0.5 #10

#########
# STRINGS
#########

s = 'hello'
# Print out 'e' using indexing
print(s[1])
# Reverse the string 'hello' using slicing:
print(s[::-1])
# Given the string hello, give two methods of producing the letter 'o' using indexing.
# Method 1:
print(s[4])
# Method 2:
print(s[-1])

#########
# LISTS
#########
# Build this list [0, 0, 0] two separate ways.
# Method 1:
list_of_zero = [0]
list_of_zero.append(0)
list_of_zero.append(0)
print(list_of_zero)

# Method 2:
print([0]*3)

# Reassign 'hello' in this nested list to say 'goodbye' instead:
list3 = [1,2,[3,4,'hello']]
list3[2][2] = "goodbye"
print(list3)

# Sort the list below:
list4 = [5, 3, 4, 6, 1]
list4.sort() #.sort() happens in place which means you have to call it again
print(list4)
print(sorted(list4))  #sorted() function will return the sorted list, doesn't happen in place

##############
# DICTIONARIES
##############
# Using keys and indexing, grab the 'hello' from the following dictionaries:

# Grab 'hello'
d = {'simple_key': 'hello'}
print(d['simple_key'])
# Grab 'hello'
d = {'k1': {'k2': 'hello'}}
print(d['k1']['k2'])
# Getting a little tricker
# Grab 'hello'
d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
# print(d['k1'])
# print(d['k1'][0])
# print(d['k1'][0]['nest_key'])
print(d['k1'][0]['nest_key'][1][0])

# This will be hard and annoying!
d = {'k1': [1, 2, {'k2': ['this is tricky', {'tough': [1, 2, ['hello']]}]}]}
# print(d['k1'])
# print(d['k1'][2])
# print(d['k1'][2]['k2'])
# print(d['k1'][2]['k2'][1])
print(d['k1'][2]['k2'][1]['tough'][2][0])
# Can you sort a dictionary? Why or why not?
# You cannot sort a dictionary because it is an unordered seq of key-value pairs which means it is unindexed
# normal dictionaries are mappings not a sequence
#########
# TUPLES
#########
# What is the major difference between tuples and lists?
# Tuples are IMMUTABLE while lists are mutable

# How do you create a tuple?
# within parens
tuple_of_things = (1, 1, 2, 2, 3, 3, "hello")

#########
# SETS
#########
# What is unique about a set?
# Unordered and unidexed, values within sets cannot be duplicated

# Use a set to find the unique values of the list below:
list5 = [1, 2, 2, 33, 4, 4, 11, 22, 3, 3, 2]
print(set(list5))


# What will be the resulting Boolean of the following pieces of code (answer fist then check by typing it in!)

# Answer before running cell
2 > 3 #false
# Answer before running cell
3 <= 2 #false
# Answer before running cell
3 == 2.0 #false
# Answer before running cell
3.0 == 3 #true
# Answer before running cell
4 ** 0.5 != 2 #false

# Final Question: What is the boolean output of the cell block below?
# two nested lists
l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]

# True or False?
l_one[2][0] >= l_two[2]['k1']
3 >= 4 #false