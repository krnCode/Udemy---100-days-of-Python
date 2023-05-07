# 19. Python Primitive Data Types

# Data Types

# String
# print("Hello"[0]) -> Subscripting
# print("Hello"[4])
# print("123" + "345")

# Integer
# print(123 + 345)
# 123_456_789

# Float
# 3.14159

# Boolean
# True
# False
# -------------------------------------


# 20. Type Error, Type Checking and Type Conversion

# num_char = len(input("What is your name? "))
# print("Your name has " + num_char + " characters.")
# print(type(num_char))
# new_num_char = str(num_char)
# print("Your name has " + new_num_char + " characters.")

# a = float(123)
# print(type(a))
# print(70 + float("100.5"))
# print(str(70) + str(100))
# -------------------------------------


# 21. [Interactive Coding Exercise] Data Types

# 🚨 Don't change the code below 👇
# two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
# digit_1 = int(two_digit_number[0])
# digit_2 = int(two_digit_number[1])
# sum_digits = digit_1 + digit_2
# print(sum_digits)
# -------------------------------------


# 22. Mathematical Operations in Python

# 3 + 5
# 7 - 4
# 3 * 2
# print(type(6 / 3))

# print(100000000000 ** 123456789)

# PEMDAS-LR
# ()
# **
# 8 /
# + -

# print(3 * (3 + 3) / 3 - 3)
# -------------------------------------


# 23. [Interactive Coding Exercise] BMI Calculator

# 🚨 Don't change the code below 👇
# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# height_float = float(height)
# weight_float = int(weight)

# bmi_calc = weight_float / (height_float ** 2)
# print(int(bmi_calc))
# -------------------------------------


# 24. Number Manipulation and F Strings in Python 

# print(round(8 / 3, 2))

# print(8 // 3)
# print(type(8 // 3))
# print(type(8 / 3))

# result = 4 / 2
# result /= 2
# print(result)

# score = 0

# User scores a point

# score += 1
# print(score)

# score = 8
# height = 1.8
# isWinning = True

# # f-string
# print(f'your score is {score}, your height is {height}, you are winning is {isWinning}')
# -------------------------------------


# 25. [Interactive Coding Exercise] Life in Weeks

# 🚨 Don't change the code below 👇
# age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# ageConverted = int(age)
# yearsLeft = 90 - ageConverted

# days = yearsLeft * 365
# months = yearsLeft * 12
# weeks = yearsLeft * 52

# print(f"You have {days} days, {weeks} weeks, and {months} months left.")
# -------------------------------------