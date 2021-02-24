# ###############
# # FUNCTIONS
# ###############
# # def keyword to create funciton
# #return keyword allows us to assign the output of function into variable

# def say_hello(name="Default name"):
#   print(f"Hello {name}")

# say_hello()
# #hello default name

# def add_num(num1, num2):
#   return num1 + num2
  
# result = add_num(1, 2)
# print(result)

# ###############
# # WARM UP
# ###############
"""
LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd
lesser_of_two_evens(2,4) --> 2
lesser_of_two_evens(2,5) --> 5
"""

# def lesser_of_two_evens(a, b):
#     return min(a,b) if a and b % 2 == 0 else max(a,b)

# print(lesser_of_two_evens(2, 10))
# print(lesser_of_two_evens(2,5))

"""
ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
"""
# def animal_crackers(text):
#   new_list = text.split()
#   return new_list[0][0] == new_list[1][0]

# print(animal_crackers('Levelheaded Llama'))
# print(animal_crackers('Crazy Kangaroo'))

"""
MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
"""
# def makes_twenty(n1, n2):
#     return (n1+n2) == 20 or n1==20 or n2==20
    
# print(makes_twenty(20,10))
# print(makes_twenty(2,3))

# ###############
# # LEVEL 1
# ###############
"""
OLD MACDONALD
Write a function that capitalizes the first and fourth letters of a name

old_macdonald('macdonald') --> MacDonald
Note: 'macdonald'.capitalize() returns 'Macdonald'
"""
# def old_macdonald(name):
#   return name[:3].capitalize() + name[3:].capitalize() if len(name) > 3 else 'Name is too short!'
  
# print(old_macdonald('macdonald'))
# print(old_macdonald('ana'))

"""
MASTER YODA: Given a sentence, return a sentence with the words reversed
master_yoda('I am home') --> 'home am I'
master_yoda('We are ready') --> 'ready are We'

.join() method allows you to join together strings in a list
>>> "--".join(['a','b','c'])
>>> 'a--b--c'
"""
# def master_yoda(text):
#   return " ".join(sorted(text.split(), reverse=True))
#         # other solution: ' '.join(text.split()[::-1])
# print(master_yoda('I am home'))
# print(master_yoda('We are ready'))

"""
ALMOST THERE
Given an integer n, return True if n is within 10 of either 100 or 200
almost_there(90) --> True
almost_there(104) --> True
almost_there(150) --> False
almost_there(209) --> True

NOTE: abs(num) returns the absolute value of a number
"""

# def almost_there(n):
#     return (90 <= n <= 110) or (190 <= n <= 210)

# print(almost_there(90))
# print(almost_there(104))
# print(almost_there(150))
# print(almost_there(209))

# ###############
# # LEVEL 2
# ###############
"""
FIND 33:
Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

has_33([1, 3, 3]) → True
has_33([1, 3, 1, 3]) → False
has_33([3, 1, 3]) → False
"""

# def has_33(nums):
#   for i in range(len(nums) - 1):
#     if (nums[i] == nums[i + 1]):
#       return True
#   return False

# print(has_33([1, 3, 3]))
# print(has_33([1, 3, 1, 3]))
# print(has_33([3, 1, 3]))

"""
PAPER DOLL
Given a string, return a string where for every character in the original there are three characters.
paper_doll('Hello') --> 'HHHeeellllllooo'
paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'
"""

# def paper_doll(text):
#     pass


# print(paper_doll('Hello'))
# print(paper_doll('Mississippi'))

# """
# BLACKJACK
# Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'

# blackjack(5,6,7) --> 18
# blackjack(9,9,9) --> 'BUST'
# blackjack(9,9,11) --> 19
# """
# def blackjack(a,b,c):
#     pass

# print(blackjack(5,6,7))
# print(blackjack(9,9,9))
# print(blackjack(9, 9, 11))

# """
# SUMMER OF '69
# Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.

# summer_69([1, 3, 5]) --> 9
# summer_69([4, 5, 6, 7, 8, 9]) --> 9
# summer_69([2, 1, 6, 9, 11]) --> 14
# """

# def summer_69(arr):
#     pass

# print(summer_69([1, 3, 5]))
# print(summer_69([4, 5, 6, 7, 8, 9]))
# print(summer_69([2, 1, 6, 9, 11]))

# # #######################
# # # CHALLENGING PROBLEMS
# # ######################

# """
# SPY GAME:
# Write a function that takes in a list of integers and returns True if it contains 00
#  spy_game([1,2,4,0,0,7,5]) --> True
#  spy_game([1,0,2,4,0,5,7]) --> True
#  spy_game([1,7,2,0,4,5,0]) --> False
# """
# def spy_game(nums):
#     pass

# print(spy_game([1,2,4,0,0,7,5]))
# print(spy_game([1,0,2,4,0,5,7]))
# print(spy_game([1, 7, 2, 0, 4, 5, 0]))

# """
# COUNT PRIMES
# Write a function that returns the number of prime numbers that exist up to and including a given number

# count_primes(100) --> 25

# By convention, 0 and 1 are not prime.
# """
# def count_primes(num):
#     pass

# print(count_primes(100))



# """
# Just for fun:
# PRINT BIG: Write a function that takes in a single letter, and returns a 5x5 representation of that letter
# print_big('a')

# out:   *  
#       * *
#      *****
#      *   *
#      *   *
# HINT: Consider making a dictionary of possible patterns, and mapping the alphabet to specific 5-line combinations of patterns.
# For purposes of this exercise, it's ok if your dictionary stops at "E".
# """

# def print_big(letter):
#     pass

# print(print_big('a'))

# # #######################
# # # FUNCS & METHODS
# # ######################

# """
# Write a function that computes the volume of a sphere given its radius.

# The volume of a sphere is given as: 4/3*3.14*r**3
# """
# def vol(rad):
#   # PEMDAS
#   return (4 / 3) * (3.14) * (rad ** 3)

# print(vol(2))

# """
# Write a function that checks whether a number is in a given range (inclusive of high and low)
# """
# def ran_check(num, low, high):
#   if num in range(low, high+1):
#     return f"{num} is in the range between {low} and {high}"
#   else:
#     return f"The number is outside the range"

# print(ran_check(5, 2, 7))
# # # 5 is in the range between 2 and 7

# # # If you only wanted to return a boolean:
# def ran_bool(num,low,high):
#     return num in range(low,high+1)

# print(ran_bool(3,1,10))