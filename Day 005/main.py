# 50. Using the for loop with Python Lists

# fruits = ["Apple", "Peach", "Pear"]

# for fruit in fruits:
#     print(fruit)
#     print(fruit + " Pie")

# print(fruits)
# -------------------------------------


# 51. [Interactive Coding Exercise] Average Height

# # 🚨 Don't change the code below 👇
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n]) # type: ignore
# # 🚨 Don't change the code above 👆


# #Write your code below this row 👇
# total_height = 0
# total_students = 0

# for heights in student_heights:
#     total_height = total_height + heights # type: ignore
#     total_students = total_students + 1

# medium_height = round(total_height / total_students)

# print(int(medium_height))
# -------------------------------------


# 52. [Interactive Coding Exercise] High Score

# # 🚨 Don't change the code below 👇
# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)
# # 🚨 Don't change the code above 👆

# #Write your code below this row 👇
# max_value = 0

# for value in student_scores:
#   if value > max_value:
#     max_value = value
#   else:
#     max_value = max_value

# print(f"The highest score in the class is: {max_value}")
# -------------------------------------


# 53. for loops and the range() function

# For Loop with range

# for number in range(1, 11, 3):
#     print(number)

# total = 0

# for number in range(1, 101):
#     total += number

# print(total)
# -------------------------------------


# 54. [Interactive Coding Exercise] Adding Even Numbers

# even_total = 0

# for number in range(0, 101):
#     if number % 2 == 0:
#         even_total += number

# print(even_total)
# -------------------------------------


# 55. [Interactive Coding Exercise] The FizzBuzz Job Interview Question

# Fizz Buzz Game

# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)
# -------------------------------------
        
