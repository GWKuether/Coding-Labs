
import random


favorite_number = 6


# random_number = random.randrange(10)

# how_far_away = random_number - favorite_number

# print(how_far_away)

# how_many_attempts = []

# def favorite_number_matcher():
#     is_this_your_number = False
#     while is_this_your_number is False:
#         random_number = random.randrange(4000)
#         how_many_attempts.append(random_number)
#         if random_number == favorite_number:
#             print("We've done it, but at what cost? " + str(len(how_many_attempts)) + " attempts!")
#             is_this_your_number = True

# favorite_number_matcher()


# for the reverse a string problem, I have to first figure out
# how long the string is. I can do this by finding the length of
# the string and subtracting one. I then have to find a way to 
# sequence it so that it runs in reverse order. I can do this by
# using a for loop. lastly, I can print the reversed string by
# adding it to an empty string.

# word = "antidisestablishmentarianism"
# reversed_word = ""
# for index in range(len(word) -1, -1, -1):
#    reversed_word += word[index]
    
# print(reversed_word)


# import string

# to capitalize the first letter of each word in a string I
# first have to figure out a way to identify when a new word
# starts. I can do this by finding the spaces in between the
# words. 

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



# did_it_work = string.capwords(capitalize_me_captain)

# print(did_it_work)

# in order to check if a word is a palindrome I first have to be
# able to flip the word in reverse. This can be done by using 
# the earlier code that we already figured out with the only
# modification being that the word is now = to the user's input.
# Once established, all that needs to be done is checking to see
# if the word that was reversed is equal to the same word in the 
# correct order. A simple if statement can check this

# word = input("Which word would you like for me to check? ")
# reversed_word = ""
# for index in range(len(word) -1, -1, -1):
#    reversed_word += word[index]

# if reversed_word == word:
#     print("That there is a palindrome")
# else:
#     print("Nope, not a palindrome!")