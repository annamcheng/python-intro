# Use for , .split(), and if tocreateaStatementthatwillprintoutwordsthatstart with 's':
# use for loop to loop through characters of string
# print out the words where at index 0 == 's'
st = 'Print only the words that start with s in this sentence'

for sletters in st.split():
  if sletters[0] == 's':
    print(sletters)

# Use range() to print all the even numbers from 0 to 10.
# Syntax for range() function: range(start,stop,step)
print([num for num in range(0, 11,2)])

# Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
print([divisible_by_3 for divisible_by_3 in range(1, 51) if divisible_by_3 % 3 == 0])

# Go through the string below and if the length of a word is even print "even!"
st2 = 'Print every word in this sentence that has an even number of letters'
print([f"This word is even: {even_word}" for even_word in st2.split() if len(even_word) % 2 == 0])

# Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
for num in range(1, 101):
  if num % 3 == 0 and num % 5 == 0:
    print('FizzBuzz')
  elif num % 3 == 0:
    print('Fizz')
  elif num % 5 == 0:
    print('Buzz')
  else:
    print(num)

# Use List Comprehension to create a list of the first letters of every word in the string below:
st3 = 'Create a list of the first letters of every word in this string'
print([letter[0] for letter in st3.split()])