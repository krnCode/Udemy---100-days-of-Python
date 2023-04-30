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