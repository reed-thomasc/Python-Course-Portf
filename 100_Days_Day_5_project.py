
# coding: utf-8

# In[ ]:


#my attempt 2/11/2025
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#EASY VERSION
# password = " "
# for character in range(0,nr_letters):
#   password += random.choice(letters)

#for character in range(0,nr_symbols):
 #   password += random.choice(symbols)

#for character in range(0,nr_numbers):
 #   password += random.choice(numbers)

# print(password)

#HARD VERSION
characters = []

for char in range(0,nr_letters):
    characters += random.choice(letters)
for char in range(0,nr_symbols):
    characters += random.choice(symbols)
for char in range(0,nr_numbers):
    characters += random.choice(numbers)

random.shuffle(characters)

password = ''.join(characters)
print(password)

#Solution

