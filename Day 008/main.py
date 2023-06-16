# 81. Functions with Inputs

# # Review: 
# # Create a function called greet()
# def greet():
#     # Write 3 print statements inside the function.
#     print("Hello")
#     print("How are you?")
#     print("Isn't the weather nice today?")

# # Call the greet() function and run your code.
# greet()


# # Function that allows for input

# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How are you {name}?")

# greet_with_name("James")
# -------------------------------------


# 82. Positional vs. Keyword Arguments

# Functions with more than 1 inputs

# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}?")

# greet_with("Helltide", "Donnas")


# Functions with keyword arguments

# def greet_with(name = "James", location = "New York City"):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}?")

# greet_with("Pamela", "Uni")
# -------------------------------------


# 83. [Interactive Coding Exercise] Paint Area Calculator

#Write your code below this line 👇
# import math

# def paint_calc(height, width, cover):
#     num_cans = math.ceil((height * width) / cover)
#     print(f"You'll need {num_cans} cans of paint.")

# #Write your code above this line 👆
# # Define a function called paint_calc() so that the code below works.   

# # 🚨 Don't change the code below 👇
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)
# -------------------------------------


# 84. [Interactive Coding Exercise] Prime Number Checker

#Write your code below this line 👇
# def prime_checker(number):
#     is_prime = True
#     for i in range(2, number):
#         if number % i == 0:
#             is_prime = False
#     if is_prime:
#         print("It's a prime number.")
#     else:
#         print("It's not a prime number.")

# #Write your code above this line 👆
    
# #Do NOT change any of the code below👇
# n = int(input("Check this number: "))
# prime_checker(number=n)
# -------------------------------------