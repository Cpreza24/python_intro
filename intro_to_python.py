# This is a comment! Python will ignore it. 

"""
this is a
multiline comment
"""

'''
this is also a multiline comment
you can use either set of quotes
'''

# this is a
# multiline comment
print("Hello, world!") # prints: Hello, world!

print(type("hello"))
# prints: <class 'str'>



#FizzBuzz Challenge 
# FizzBuzz
# Print the numbers from 1 to 50
# For multiples of 3, print "Fizz" instead of the number
# For multiples of 5, print "Buzz" instead of the number
# For numbers which are multiples of both 3 and 5, print "FizzBuzz"



for num in range(1, 51):
    if num % 3 == 0 and num % 5 == 0:
        print('FizzBuzz')
    elif num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print('Buzz')
    else:
        print(num)
    


# 99 Bottles of Beer on the Wall
# Print the lyrics to the song starting from 99 down to 0

bottles = 99

# while bottles > 0:
    # if bottles > 1:
    #     print(f'{bottles} bottles of beer on the wall, {bottles} bottles of beer, take one down, pass it around, {bottles} bottles of beer on the wall')
    #     bottles -= 1
    # elif bottles == 1:
    #     print(f'{bottles} bottle of beer on the wall, {bottles} bottle of beer, take one down, pass it around, {bottles  - 1} bottle of beer on the wall')
    #     bottles -= 1
    # elif bottles >= 0:
    #     print('no more bottles of beer on the wall')

while bottles > 0:
    if bottles == 1:
        print(f"{bottles} bottle of beer on the wall, {bottles} bottle of beer.")
        print("Take one down and pass it around, no more bottles of beer on the wall.")
    else:
        print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
        print(f"Take one down and pass it around, {bottles - 1} {'bottle' if bottles - 1 == 1 else 'bottles'} of beer on the wall.")
    bottles -= 1
print("No more bottles of beer on the wall, no more bottles of beer.")

    
    # if bottles > 1:
    #     print(f'take one down, pass it around, {bottles} bottles of beer on the wall')
    # elif bottles == 1:
    #     print(f'take one down, pass it around, {bottles} bottle of beer on the wall')
    # else:
    #     print('no more bottles of beer on the wall')

# Example:
# 99 bottles of beer on the wall, 99 bottles of beer.
# Take one down and pass it around, 98 bottles of beer on the wall.
# ...
# No more bottles of beer on the wall, no more bottles of beer.



# Sum of Even Numbers
# Calculate the sum of all even numbers from 1 to 100

total = 0

for number in range(1, 101):
    if number % 2 == 0:
        total += number

print("The sum of even numbers from 1 to 100 is:", total)







# Word Reverser
# Ask the user to enter a word and then print it reversed.

word = input("Enter a word: ")
reversed_word = word[::-1]
print(reversed_word)

# Print the word reversed

# Example:
# Input: python
# Output: nohtyp


# Count the number of vowels in a word or sentence

text = input("Enter a word or sentence: ")
vowels = ['a', 'e', 'i', 'o', 'u']
vowel_count = 0

for vowel in vowels:
    for letter in text:
        if letter == vowel:
            vowel_count += 1
print(vowel_count)



# Palindrome Checker
# A palindrome is a word that reads the same backward and forward
# Example: "racecar", "madam", "level"

word = input("Enter a word: ")
reversed_word = word[::-1]

if reversed_word == word:
    print('true')
else:
    print('false')

# Check if the word is a palindrome and print True or False

# Example:
# Input: racecar
# Output: True




# Password Strength Checker
# Ask the user to enter a password.
# Check if the password is strong.
# A strong password must:
# - Be at least 8 characters long
# - Contain at least one uppercase letter
# - Contain at least one lowercase letter
# - Contain at least one digit
# - Contain at least one special character (!, @, #, $, %, etc.)

password = input("Enter a password: ")

password_strength = False

if len(password) < 8:
    print("This is not enough characters!")

if not any(char.isupper() for char in password):
    print("This does not have an upper case!")

if not any(char.islower() for char in password):
    print("This does not have an lower case!") 

if not any(char.isdigit() for char in password):
    print("This does not have a digit!")

if not any(char.isalnum() for char in password):
    print("This does not have a special character!")

if password_strength == True:
    print("You have a strong password!")

# Write code to check each of these rules and print:
# - "Strong password!" if all rules are met
# - Otherwise, print which rules are missing

# Example:
# Enter a password: Pass12
# Output:
# Password is too short.
# Password must contain at least one special character.

