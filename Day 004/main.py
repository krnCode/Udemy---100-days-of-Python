41. Random Module

import random
import my_module

random_integer = random.randint(1, 10)
print(random_integer)

# print(my_module.pi)

# random_float = random.random()
# print(random_float)

random_float2 = random.random() * 5
print(random_float2)

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")
-------------------------------------


42. [Interactive Coding Exercise] Heads or Tails

Remember to use the random module
Hint: Remember to import the random module here at the top of the file. 🎲
	 
Write the rest of your code below this line 👇
import random

toss = random.randint(0, 1)

if toss == 1:
    print("Heads")
else:
    print("Tails")
-------------------------------------


43. Understanding the Offset and Appending Items to Lists

states_of_america = ["Delaware","Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", 
"New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine",
"Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska",
"Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(states_of_america)

states_of_america[1] = "Pencilvania"
print(states_of_america)

states_of_america.append("Angelaland")
print(states_of_america)

states_of_america.extend(["Angelaland", "Jack Bauer Land"])
print(states_of_america)
-------------------------------------


44. [Interactive Coding Exercise] Banker Roulette - Who will pay the bill?

# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
random_pick = random.randint(0, len(names) - 1)
print(f"{names[random_pick]} is going to buy meal today!")
-------------------------------------


45. IndexErrors and Working with Nested Lists

states_of_america = ["Delaware","Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", 
"New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine",
"Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska",
"Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

num_of_states = len(states_of_america) - 1

print(states_of_america[num_of_states])

dirty_dozen = ["Strawberry", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

fruits = ["Strawberry", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]
print(dirty_dozen)
-------------------------------------


46. [Interactive Coding Exercise] Treasure Map

# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
pos_list = int(position[1]) - 1
pos_item = int(position[0]) - 1

map[pos_list][pos_item] = " X" 

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
-------------------------------------


