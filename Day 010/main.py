# 99. Functions with Outputs

# Functions with outputs
# def format_name(f_name, l_name):
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()

#     return f"{formated_f_name} {formated_l_name}"


# print(format_name("pAuLO", "santAna"))
# -------------------------------------


# 100. Multiple return values


# def format_name(f_name, l_name):
#     if f_name == "" or l_name == "":
#         return
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()

#     return f"Result: {formated_f_name} {formated_l_name}"


# print(
#     format_name(input("What is your first name? "), input("What is your last name? "))
# )
# -------------------------------------


# 101. [Interactive Coding Exercise] Days in Month


# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False


# def days_in_month(year, month):
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if is_leap(year) == True:
#         month_days[1] = 29
#         return month_days[month - 1]
#     return month_days[month - 1]


# # 🚨 Do NOT change any of the code below
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)
# -------------------------------------


# 102. Docstrings


# def format_name(f_name, l_name):
#     """Take a first and last name and format it to return the title case version of the name."""

#     if f_name == "" or l_name == "":
#         return
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()

#     return f"Result: {formated_f_name} {formated_l_name}"


# print(
#     format_name(input("What is your first name? "), input("What is your last name? "))
# )
# -------------------------------------


# 103. Calculator Part 1: Combining Dictionaries and Functions

# Calculator


# # Add
# def add(n1, n2):
#     return n1 + n2


# # Subtract
# def subtract(n1, n2):
#     return n1 - n2


# # Multiply
# def multiply(n1, n2):
#     return n1 * n2


# # Divide
# def divide(n1, n2):
#     return n1 / n2


# # Calculations
# operations = {
#     "+": add,
#     "-": subtract,
#     "*": multiply,
#     "/": divide,
# }


# num1 = int(input("What's the first number? "))


# for symbol in operations:
#     print(symbol)


# operation_symbol = input("Pick an operation from the line above: ")

# num2 = int(input("What's the second number? "))

# calculation_function = operations[operation_symbol]

# answer = calculation_function(num1, num2)

# print(f"{num1} {operation_symbol} {num2} = {answer}")
# -------------------------------------


# # 104. Print vs. Return


# # Add
# def add(n1, n2):
#     return n1 + n2


# # Subtract
# def subtract(n1, n2):
#     return n1 - n2


# # Multiply
# def multiply(n1, n2):
#     return n1 * n2


# # Divide
# def divide(n1, n2):
#     return n1 / n2


# # Calculations
# operations = {
#     "+": add,
#     "-": subtract,
#     "*": multiply,
#     "/": divide,
# }


# num1 = int(input("What's the first number? "))


# for symbol in operations:
#     print(symbol)

# operation_symbol = input("Pick an operation from the line above: ")
# num2 = int(input("What's the second number? "))
# calculation_function = operations[operation_symbol]
# first_answer = calculation_function(num1, num2)

# print(f"{num1} {operation_symbol} {num2} = {first_answer}")

# operation_symbol = input("Pick another operation: ")
# num3 = int(input("What's the next number? "))
# calculation_function = operations[operation_symbol]
# second_answer = calculation_function(first_answer, num3)

# print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")
# -------------------------------------


# 105. While Loops, Flags and Recursion


# # Add
# def add(n1, n2):
#     return n1 + n2


# # Subtract
# def subtract(n1, n2):
#     return n1 - n2


# # Multiply
# def multiply(n1, n2):
#     return n1 * n2


# # Divide
# def divide(n1, n2):
#     return n1 / n2


# # Calculations
# operations = {
#     "+": add,
#     "-": subtract,
#     "*": multiply,
#     "/": divide,
# }


# def calculator():
#     num1 = int(input("What's the first number? "))

#     for symbol in operations:
#         print(symbol)

#     should_continue = True

#     while should_continue:
#         operation_symbol = input("Pick an operation: ")
#         num2 = int(input("What's the next number? "))
#         calculation_function = operations[operation_symbol]
#         answer = calculation_function(num1, num2)

#         print(f"{num1} {operation_symbol} {num2} = {answer}")

#         calc_continue = input(
#             f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: "
#         )

#         if calc_continue == "n":
#             should_continue = False
#             calculator()

#         else:
#             num1 = answer


# calculator()
# -------------------------------------


# 106. Calculator Finishing Touches and Bug Fixes
# from art import logo


# # Add
# def add(n1, n2):
#     return n1 + n2


# # Subtract
# def subtract(n1, n2):
#     return n1 - n2


# # Multiply
# def multiply(n1, n2):
#     return n1 * n2


# # Divide
# def divide(n1, n2):
#     return n1 / n2


# # Calculations
# operations = {
#     "+": add,
#     "-": subtract,
#     "*": multiply,
#     "/": divide,
# }


# def calculator():
#     print(logo)
#     num1 = float(input("What's the first number? "))

#     for symbol in operations:
#         print(symbol)

#     should_continue = True

#     while should_continue:
#         operation_symbol = input("Pick an operation: ")
#         num2 = float(input("What's the next number? "))
#         calculation_function = operations[operation_symbol]
#         answer = calculation_function(num1, num2)

#         print(f"{num1} {operation_symbol} {num2} = {answer}")

#         calc_continue = input(
#             f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: "
#         )

#         if calc_continue == "n":
#             should_continue = False
#             calculator()

#         else:
#             num1 = answer


# calculator()
# -------------------------------------
