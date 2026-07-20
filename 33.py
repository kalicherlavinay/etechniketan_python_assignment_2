# ==========================================================
#               PYTHON ASSIGNMENT 3
#               Question 33
# Find all indexes of 'p' in the given string.
# ==========================================================

s1 = "practice is important to perfectly learn python"

indexes = []

for i in range(len(s1)):
    if s1[i] == 'p':
        indexes.append(i)

print("Indexes of 'p':", indexes)


#Question 34
# Count the number of palindrome strings whose length is
# greater than 2 using slicing.

words = ["aba", "abc", "1991", "madam", "python", "aa"]

count = 0

for word in words:
    if len(word) > 2 and word == word[::-1]:
        count += 1

print("Palindrome Count:", count)

# Sample Output:
# Palindrome Count: 3


#               Question 35
# Find all unique words with length greater than or equal to
# 4 that start with 'w' or 'W'.

s1 = "How much wood would a woodchuck chuck if a Woodcutter could chuck wood to build a wooden house to woo his wife"

words = s1.split()

result = []

for word in words:
    if len(word) >= 4 and (word.startswith("w") or word.startswith("W")):
        if word not in result:
            result.append(word)

print("Required Words:", result)

# Sample Output:
# Required Words: ['wood', 'would', 'woodchuck', 'Woodcutter', 'wooden', 'wife']


#               Question 36
# Read a string from the user and display the frequency
# of each character using a dictionary.


text = input("Enter a string: ")

count = {}

for ch in text:
    if ch in count:
        count[ch] += 1
    else:
        count[ch] = 1

print("Character Frequency:", count)

# Sample Input:
# google.com

# Sample Output:
# Character Frequency:
# {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}


#               Question 37
# Find the costliest product from the given dictionary.


products = {
    "soap": 50,
    "oil": 200,
    "laptop": 60000,
    "phone": 25000,
    "mouse": 500
}

costliest_product = max(products, key=products.get)

print("Costliest product is:", costliest_product)

# Sample Output:
# Costliest product is: laptop


#               Question 38
# Remove the specified keys from the given dictionary.


d = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New York"
}

keys_to_remove = ["name", "salary"]

for key in keys_to_remove:
    if key in d:
        d.pop(key)

print("Updated Dictionary:", d)

# Sample Output:
# Updated Dictionary: {'age': 25, 'city': 'New York'}


#               Question 39
# Write a Python program that takes an integer as input and
# counts down from that number to 0 using a while loop.
# Print "Blast!" when the count reaches 0.


num = int(input("Enter a number: "))

while num >= 0:
    if num == 0:
        print("Blast!")
    else:
        print(num)

    num -= 1

# Sample Input:
# 5

# Sample Output:
# 5
# 4
# 3
# 2
# 1
# Blast!


#               Question 40
# Write a Python program to continuously take student's
# marks (0-100) as input and display the grade using
# if-elif-else. Ask the user if they want to continue.


print("Welcome to the Grade Checker Program!")

while True:

    marks = float(input("Enter your marks (0-100): "))

    if marks >= 90 and marks <= 100:
        print("Your Grade is A+")

    elif marks >= 80:
        print("Your Grade is A")

    elif marks >= 70:
        print("Your Grade is B")

    elif marks >= 60:
        print("Your Grade is C")

    elif marks >= 50:
        print("Your Grade is D")

    else:
        print("Your Grade is Fail")

    choice = input("Do you want to check another grade? (yes/no): ")

    if choice.lower() == "no":
        print("Thank You!")
        break

# Sample Output:
# Welcome to the Grade Checker Program!
# Enter your marks (0-100): 85
# Your Grade is A
# Do you want to check another grade? (yes/no): yes
# Enter your marks (0-100): 45
# Your Grade is Fail
# Do you want to check another grade? (yes/no): no
# Thank You!


#               Question 41
# Write a Python program to print:
# "Fizz" if the number is divisible by 3,
# "Buzz" if the number is divisible by 5,
# "FizzBuzz" if the number is divisible by both 3 and 5,
# otherwise print the number itself.


num = int(input("Enter a number: "))

if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")

elif num % 3 == 0:
    print("Fizz")

elif num % 5 == 0:
    print("Buzz")

else:
    print(num)

# Sample Input:
# 15

# Sample Output:
# FizzBuzz


#               Question 42
# Create a password authentication system.
# Allow the user only 3 attempts to enter the correct
# password. Print "Access Granted" if correct, otherwise
# print "Access Denied" after 3 failed attempts.


password = "admin123"

attempts = 0

while attempts < 3:

    user_password = input("Enter Password: ")

    if user_password == password:
        print("Access Granted")
        break

    else:
        attempts += 1
        print("Wrong Password!")

if attempts == 3:
    print("Access Denied")

# Sample Output:
# Enter Password: abc
# Wrong Password!
# Enter Password: 123
# Wrong Password!
# Enter Password: admin123
# Access Granted


#               Question 43
# Create a Simple Coin Toss Game using the random module.
# The user guesses "heads" or "tails". The program checks
# the guess, displays the result, and asks if the user
# wants to play again.


import random

print("Welcome to the Simple Coin Toss Game!")

while True:

    guess = input("Guess 'heads' or 'tails': ").lower()

    if guess != "heads" and guess != "tails":
        print("Invalid input! Please enter 'heads' or 'tails'.")
        continue

    toss = random.choice(["heads", "tails"])

    print("Coin shows:", toss)

    if guess == toss:
        print("You guessed it right!")
    else:
        print("Wrong guess!")

    choice = input("Do you want to play again? (yes/no): ").lower()

    if choice == "no":
        print("Thanks for playing!")
        break

# Sample Output:
# Welcome to the Simple Coin Toss Game!
# Guess 'heads' or 'tails': heads
# Coin shows: tails
# Wrong guess!
# Do you want to play again? (yes/no): yes
# Guess 'heads' or 'tails': tails
# Coin shows: tails
# You guessed it right!
# Do you want to play again? (yes/no): no
# Thanks for playing!


