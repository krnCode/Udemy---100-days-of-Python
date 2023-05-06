# 29. Control Flow with if / else and Conditional Operators

# print("Welcome to the rollercoaster!")
# height = int(input("What is your hehight in cm? "))

# if height >= 120:
#     print("You can ride the rollercoaster!")
# else:
#     print("Sorry, you have to grow taller before you can ride.")
# -------------------------------------


# 30. [Interactive Coding Exercise] Odd or Even? Introducing the Modulo

# # 🚨 Don't change the code below 👇
# number = int(input("Which number do you want to check? "))
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# if number % 2 != 0:
#     print("This is an odd number.")
# else:
#     print("This is an even number.")
# -------------------------------------


# 31. Nested if statements and elif statements

# print("Welcome to the rollercoaster!")
# height = int(input("What is your hehight in cm? "))

# if height >= 120:
#     print("You can ride the rollercoaster!")

#     age = int(input("What is your age? "))
#     if age < 12:
#         print("Please pay $5.")
#     elif age <= 18:
#         print("Please pay $7.")
#     else:
#         print("Please pay $12.")
    
# else:
#     print("Sorry, you have to grow taller before you can ride.")
# -------------------------------------


# 32. [Interactive Coding Exercise] BMI 2.0

# # 🚨 Don't change the code below 👇
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
# # 🚨 Don't change the code above 👆

# # Write your code below this line 👇
# bmiValue = round(weight / height ** 2)

# if bmiValue <= 18.5:
#     print(f"Your BMI is {bmiValue}, you are underweight.")
# elif bmiValue < 25:
#     print(f"Your BMI is {bmiValue}, you have a normal weight.")
# elif bmiValue < 30:
#     print(f"Your BMI is {bmiValue}, you are slightly overweight.")
# elif bmiValue < 35:
#     print(f"Your BMI is {bmiValue}, you are obese.")
# else:
#     print(f"Your BMI is {bmiValue}, you are clinically obese.")
# -------------------------------------


# 33. [Interactive Coding Exercise] Leap Year

# # 🚨 Don't change the code below 👇
# year = int(input("Which year do you want to check? "))
# # 🚨 Don't change the code above 👆

# # Write your code below this line 👇
# if year % 4 == 0:
#     if  year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap year.")
#         else:
#             print("Not leap year.")
#     else:
#         print("Leap year.")
# else:
#     print("Not leap year.")
# -------------------------------------


# 34. Multiple If Statements in Succession

# print("Welcome to the rollercoaster!")
# height = int(input("What is your hehight in cm? "))

# if height >= 120:
#     print("You can ride the rollercoaster!")

#     age = int(input("What is your age? "))
#     if age < 12:
#         bill = 5
#         print("Child tickets are $5.")
#     elif age <= 18:
#         bill = 7
#         print("Youth tickets are $7.")
#     else:
#         bill = 12
#         print("Adult tickets are pay $12.")
    
#     wants_photo = input("Do you want a photo taken? Y or N. ")

#     if wants_photo == "Y":
#         # Add $3 to their bill 
#         bill += 3

#         print(f"Your final bill is ${bill}")
# else:
#     print("Sorry, you have to grow taller before you can ride.")
# -------------------------------------


# 35. [Interactive Coding Exercise] Pizza Order Practice

# # 🚨 Don't change the code below 👇
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# # 🚨 Don't change the code above 👆

# # Write your code below this line 👇

# # Total bill
# pizzaTotal = 0

# # Pizza prices
# pizzaSmallPrice = 15
# pizzaMediumPrice = 20
# pizzaLargePrice = 25


# # Toppings prices
# pepperoniSmall = 2
# pepperoniMedium = 3
# extraCheesePrice = 1


# # Pizza Price Calculation Logic
# if size == "S":
#     pizzaTotal += pizzaSmallPrice
# elif size == "M":
#     pizzaTotal += pizzaMediumPrice
# else:
#     pizzaTotal += pizzaLargePrice


# # Toppings Calculation Logic
# if add_pepperoni == "Y" and size == "S":
#     pizzaTotal += pepperoniSmall
# elif add_pepperoni == "Y" and size == "M":
#     pizzaTotal += pepperoniMedium
# elif add_pepperoni == "Y" and size == "L":
#     pizzaTotal += pepperoniMedium
# else:
#     pizzaTotal

# if extra_cheese == "Y":
#     pizzaTotal += extraCheesePrice


# print(f'Your final bill is: ${pizzaTotal}.')
# -------------------------------------


#  36. Logical Operators

# print("Welcome to the rollercoaster!")
# height = int(input("What is your hehight in cm? "))

# if height >= 120:
#     print("You can ride the rollercoaster!")

#     age = int(input("What is your age? "))
#     if age < 12:
#         bill = 5
#         print("Child tickets are $5.")
#     elif age <= 18:
#         bill = 7
#         print("Youth tickets are $7.")
#     elif age >= 45 and age <= 55:
#         bill = 0
#         print("Youth tickets are $0.")
#     else:
#         bill = 12
#         print("Adult tickets are pay $12.")
    
#     wants_photo = input("Do you want a photo taken? Y or N. ")

#     if wants_photo == "Y":
#         # Add $3 to their bill 
#         bill += 3

#         print(f"Your final bill is ${bill}")
# else:
#     print("Sorry, you have to grow taller before you can ride.")
# -------------------------------------


# 37. [Interactive Coding Exercise] Love Calculator

# # 🚨 Don't change the code below 👇
# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# name1Lower = name1.lower()
# name2Lower = name2.lower()

# counter1 = name1Lower.count("t") + name1Lower.count("r") + name1Lower.count("u") + name1Lower.count("e") + name2Lower.count("t") + name2Lower.count("r") + name2Lower.count("u") + name2Lower.count("e")
# counter2 = name1Lower.count("l") + name1Lower.count("o") + name1Lower.count("v") + name1Lower.count("e") + name2Lower.count("l") + name2Lower.count("o") + name2Lower.count("v") + name2Lower.count("e")

# counterTotal = int(str(counter1) + str(counter2))


# if counterTotal < 10 or counterTotal > 90:
#     print(f"Your score is {counterTotal}, you go together like coke and mentos.")

# elif counterTotal >= 40 and counterTotal <= 50:
#     print(f"Your score is {counterTotal}, you are alright together.")

# else:
#     print(f"Your score is {counterTotal}.")