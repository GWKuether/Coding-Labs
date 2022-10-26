
from distutils.command.install_egg_info import to_filename
import random


favorite_number = 6


random_number = random.randrange(10)

how_far_away = random_number - favorite_number

print(how_far_away)

how_many_attempts = []

def favorite_number_matcher():
    is_this_your_number = False
    while is_this_your_number is False:
        random_number = random.randrange(4000)
        how_many_attempts.append(random_number)
        if random_number == favorite_number:
            print("We've done it, but at what cost? " + str(len(how_many_attempts)) + " attempts!")
            is_this_your_number = True

favorite_number_matcher()


# for the reverse a string problem, I have to first figure out
# how long the string is. I can do this by finding the length of
# the string and subtracting one. I then have to find a way to 
# sequence it so that it runs in reverse order. I can do this by
# using a for loop. lastly, I can print the reversed string by
# adding it to an empty string.

word = "antidisestablishmentarianism"
reversed_word = ""
for index in range(len(word) -1, -1, -1):
   reversed_word += word[index]
    
print(reversed_word)


import string

# to capitalize the first letter of each word in a string I
# first have to figure out a way to identify when a new word
# starts. I can do this by finding the spaces in between the
# words. Before I do that, however, I have to determine the
# length of the string that is being input so that I can create
# a range that will shuffle through the entire index of the string.
# I can do this by using the len function, meaning that my range
# will be from 1 to the full length of the string. Once I've 
# determined the range, I can shuffle through the index of the
# string and analyze each individual character used. But, like
# I originally stated, I am specifically looking to identify the
# spaces so that the preceding letter can be capitalized. I can
# do this by finding the spaces using the index - 1 = " " feature.
# in this way, it will find the spaces and then will be able
# to determine that the next character is the first letter of the
# word. This character can then be capitalized using the .upper
# function. Lastly, I have to put together a new string using the
# altered original string with newly added capital letters.
# The if statement will shuffle through and add all characters
# if they need capitalizing or not. Then I just print the new string.

capitalize_me_captain = '''this is the string of which i am now 
going to attempt to capitalize the first letter of each word'''


storage = ""

for index in range(1, len(capitalize_me_captain)):
    if capitalize_me_captain[index - 1] == " ":
        capitalize_me_captain[index].upper()
        storage += capitalize_me_captain[index].upper()
    else:
        storage += capitalize_me_captain[index]

print(storage)



did_it_work = string.capwords(capitalize_me_captain)

print(did_it_work)

# in order to check if a word is a palindrome I first have to be
# able to flip the word in reverse. This can be done by using 
# the earlier code that we already figured out with the only
# modification being that the word is now = to the user's input.
# Once established, all that needs to be done is checking to see
# if the word that was reversed is equal to the same word in the 
# correct order. A simple if statement can check this

word = input("Which word would you like for me to check? ")
reversed_word = ""
for index in range(len(word) -1, -1, -1):
   reversed_word += word[index]

if reversed_word == word:
    print("That there is a palindrome")
else:
    print("Nope, not a palindrome!")



# in order to figure out if a number is a happy number I first
# have to find a way to split a number into its square parts. I 
# also have to separate the digits if it is a number that is 
# larger than 9. 

for num in range(0, 100):
    if num < 10:
        num / 2
        if num / 2 == 1:
            print(f"{num} is a happy number")
        else:
            print(f"{num} is a sad number")



# to figure out how to print all prime numbers between 0 and 100
# you must first figure out how to determine if a number is prime.
# You can do this using the modulus operator. This will determine
# if there is a remainder when you divide. If there is a remainder
# then the number is prime. If the remainder is 0 then it can be
# divided. So now that we've determined that, we need to find a
# way to shuffle through each number between 0 and 100 and check
# to see how they divide. We can use the range feature and a for
# loop to shuffle through each individual number. but we still 
# need to determine the number that is being divided, which means
# that we need to create another range to make our equation work.
# so we need to run our original for loop range and then nest 
# another for loop within with the range including the original
# for loop number. This way we can use the modulus operator to
# shuffle through every number up until our first number and see
# if there is a remainder of 0. If there is a remainder of 0, 
# then it is not a prime number and will not print. Otherwise,
# it will be a prime number and will print to the console. Lastly,
# The number has to be greater than 1 for us to start the division,
# so we can put an if statement making sure that the number is
# greater than 1.

for num in range(0, 100):
    if num > 1:
        for num_2 in range(2, num):
            if (num % num_2) == 0:
                break
        else:
            print(num)





# In order to figure out how to print the fibonacci sequence, 
# I must be able to continually add up two numbers, and make them 
# equal to the third number. I then need to add the second number 
# and the third number and make that equal to the 4th number.
# This means that I should be shuffling through a range and adding
# numbers until the math checks out.

num_2 = 1

for num in range(1,20):
    if num == 1:
        printer = num
        print(printer)
    else:
        num = num_2
        printer = num + num_2    
        print(printer)
        

