# ####################
# # PYTHON STATEMENTS
# ###################
# # CONTROL FLOW
# ###################
# # We often only want certain code to execute when a particular condition has been met
# # Syntax makes use of colons and indentation (white space)
# # To control this flow of logic, we can use keywords: if, elif, else

# # Syntax for if statement
# if True:
#   print("This condition is True")

# # Syntax for if/else statement
# if True:
#   print("This condition is True")
# else:
#   print("This is something else")

# # Syntax for elif statement
# # If you want to check multiple conditions before that else statement, use elif
# if False:
#   print("This is false")
# elif True:
#   print("This elif condition is True")
# else:
#   print('This is something else')

# ###################
# # FOR LOOPS
# ###################
# # Syntax for a for loop
# my_iterable = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# #item_name is a variable that we initiate
# #represents the iterable objects in the list
# for item_name in my_iterable:
#   print(item_name)

# for num in my_iterable:
#   if num % 2 == 0:
#     print('Even number: {}'.format(num))
#   else:
#     print(f'Odd Number: {num}')

# #Indentation differences
# list_sum = 0
# for num in my_iterable:
#   list_sum = list_sum + num
#   print(list_sum)  #will print out running tally of sum; 1,3,5,10,15....55
# print(list_sum)  # will print out the sum of all numbers; 55

# # can iterate through tuples as well
# # TUPLE UNPACKING
# my_list = [(1, 2), (3, 4)]
# for a, b in my_list:
#   print(a) # 1, 3
#   print(b)  # 2, 4
  
# # when you iterate through dictionaries, you only iterate through the keys!
# icecream = {'flavor': 'vanilla', 'shop': 'van leeuwen'}
# for item in icecream:
#   print(item)  # {flavor, shop}
  
# # if you want to iterate through the values, use .items() on variable
# for item in icecream.items():
#   print(item)  # {vanilla, van leeuwen}
  
# # Dictionary also allows for unpacking
# for key, value in icecream.items():
#   print(key)
#   print(value)

# # NOTE: Dictionaries are unordered so they wont always print in order in larger data sets.

# ###################
# # WHILE LOOPS
# ###################
# # While loops will continue to execute a block of code WHILE some condition remains True
# # Ex: while my dog is still hungry, keeping feeding my dog
# x = 0
# while x < 5:
#   print(f'The current value of x is {x}')
#   #exit statement
#   x += 1
# else:
#   print("X IS NOT LESS THAN 5")

# # NOTE KEYWORDS: BREAK, CONTINUE, PASS
# # We can use these statements in our loops to add additional functionality for various cases.
# # break: Breaks out of the current closest enclosing loop
# # continue: Goes to top of the closest enclosing loop
# # pass: Does nothing at all
# x = 0
# while x < 5:
#   # if x is ever 2, break out of loop.
#   if x == 2:
#     break
#   print(x)
#   x += 1

# name = 'Anna'
# for letter in name:
#   if letter == 'a':
#     continue
#   print(letter)  # Ann
  
# x = [1, 2, 3]
# for item in x:
#   pass # tell computer to do nothing at all
# print('This is the end of my script')

# ###################
# # USEFUL OPERATORS
# ###################
# # range keyword has start stop step size
# # range(stop) -> range object
# # range(start, stop[, step]) -> range object
# mylist = [1, 2, 3]
# for num in range(3,10,2):
#   print(num)  # print every other num start from 3-10 not including 10; 3,5,7,9
  
# enumerate function
# takes in any iterable object and return some sort of index counter and then the object itself
# index_count = 0
# word = 'abcde'

# for letter in word:
#   print('At index {} the letter is {}'.format(index_count, letter))
#   index_count += 1
# At index 0 the letter is a
# At index 0 the letter is b
# At index 0 the letter is c
# At index 0 the letter is d
# At index 0 the letter is e

# index_count2 = 0
# word2 = 'fghijk'
# for letter in word2:
#   print(word2[index_count2])
#   index_count2 += 1

# word2 = 'fghijk'
# for letter in enumerate(word2):
#   print(letter)
#   # returns tuples

# # (0, 'f')
# # (1, 'g')
# # (2, 'h')
# # (3, 'i')
# # (4, 'j')
# # (5, 'k')

# # zip function
# # zip together lists and pair up items so they match together - must iterate thru it for it to return a value
# mylist1 = [1, 2, 3]
# mylist2 = ['a', 'b', 'c']
# for item in zip(mylist1,mylist2):
#   print(item)
# # (1, 'a')
# # (2, 'b')
# # (3, 'c')

# # put zip in list
# print(list(zip(mylist1, mylist2)))
# # [(1, 'a'), (2, 'b'), (3, 'c')]

# #IN OPERATOR
# # check if an item is in a list
# print(2 in [1, 2, 3])  # true
# print('mykey' in {'mykey': 123}) # true

# d = {'mykey': 345}
# print(345 in d.values())  # true
# print(345 in d.keys())  # false

# # MIN/MAX will return min/max of a list
# mynums = [10, 20, 30, 40, 50]
# print(min(mynums)) # 10
# print(max(mynums)) # 50

# #import functions from library using IMPORT KEYWORD

# # from random library, import shuffle function
# # shuffles a list; in place function, happens in place
# random_nums = [4, 9, 5, 7, 2]
# from random import shuffle
# random_list = shuffle(random_nums)  # none bc shuffle function is happening in place
# print(random_nums) # call the list of nums again to get result

# # to grab random integer from 0 to 100
# from random import randint
# #save in a variable to use it later
# x = randint(0, 100)
# print(x)

# # USER INPUT function
# # input always accepts anything you enter in as a STRING
# inputresult = input('Enter a number here: ')
# print(inputresult)

# #####################
# # LIST COMPREHENSION
# #####################
# Unique way of quickly creating a list w/ Python
# If you find yourself using a loop along with .append() to create a list, LIST COMPREHENSION are a good alternative!
# Syntax for list comprehension: [expression for item in iterable if condition == True]

# flattened out for loop
mystring = 'hello'
sayhello = []
for letter in mystring:
  sayhello.append(letter)
print(sayhello)

for letter in mystring:
  sayhello = [letter for letter in mystring]
print(sayhello)

print([x for x in "word two"])  # ['w', 'o', 'r', 'd', ' ', 't', 'w', 'o']

print([num**2 for num in range(0, 11)])  #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# can perform operation on the expression #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
