# 91. The Python Dictionary: Deep Dive

# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.",
#     "Function": "A piece of code that you can easily call over and over again.",
#     }


# Retrieving items for dictionary.
# print(programming_dictionary["Function"])


# Adding new items to dictionary.
# programming_dictionary["Loop"] = "The action of doing something over and over again."
# print(programming_dictionary)


# Create an empty dictionary.
# empty_dictionary = {}


# Wipe an existing dictionary.
# programming_dictionary = {}
# print(programming_dictionary)


# Edit an item in a dictionary.
# programming_dictionary["Bug"] = "A moth in your computer."
# print(programming_dictionary)


# Loop through a dictionary.
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])
# -------------------------------------


# 92. [Interactive Coding Exercise] Grading Program

# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }
# 🚨 Don't change the code above 👆


#TODO-1: Create an empty dictionary called student_grades.
# student_grades = {}


#TODO-2: Write your code below to add the grades to student_grades.👇
# Scores 91 - 100: Grade = "Outstanding"
# Scores 81 - 90: Grade = "Exceeds Expectations"
# Scores 71 - 80: Grade = "Acceptable"
# Scores 70 or lower: Grade = "Fail"

# for student in student_scores:
#     if student_scores[student] >= 91:
#         student_grades[student] = "Outstanding"
#     elif student_scores[student] >= 81 and student_scores[student] < 90:
#         student_grades[student] = "Exceeds Expectations"
#     elif student_scores[student] >= 71 and student_scores[student] < 80:
#         student_grades[student] = "Acceptable"
#     else:
#         student_grades[student] = "Fail"


# # 🚨 Don't change the code below 👇
# print(student_grades)
# -------------------------------------


# 93. Nesting Lists and Dictionaries

# Nesting
# capitals = { 
#     "France": "Paris",
#     "Germany": "Berlin",
# }

# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Belin", "Hamburg", "Stuttgart"],
# }

# Nesting dictionary in a dictionary

# travel_log = {
#     "France": {
#         "cities_visited": ["Paris", "Lille", "Dijon"],
#         "total_visits": 12,
#         },
#     "Germany": {
#         "cities_visited": ["Belin", "Hamburg", "Stuttgart"],
#         "total_visits": 5,
#         }
# }

# Nesting dictionary in a list

# travel_log = [
#     {
#         "country": "France",
#         "cities_visited": ["Paris", "Lille", "Dijon"],
#         "total_visits": 12}, 
#     {
#         "country": "Germany",
#         "cities_visited": ["Belin", "Hamburg", "Stuttgart"],
#         "total_visits": 5},
# ]
# -------------------------------------
