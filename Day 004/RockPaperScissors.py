import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

# Player logic
player_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. ") 
if int(player_choice) == 0:
    print(rock)
elif int(player_choice) == 1:
    print(paper)
elif int(player_choice) == 2:
    print(scissors)
else:
    print("You typed an invalid number or character, you lose!")


# Computer logic
cpu_roll = random.randint(0, 2)
print("Computer choose: ")

if cpu_roll == 0:
    print(rock)
elif cpu_roll == 1:
    print(paper)
else:
    print(scissors)


# Game rules

if int(player_choice) == cpu_roll:
    print("It's a draw!")
elif int(player_choice) == 0 and cpu_roll == 2:
    print("You won!")
elif int(player_choice) == 1 and cpu_roll == 0:
    print("You won!")
elif int(player_choice) == 2 and cpu_roll == 1:
    print("You won!")
elif int(player_choice) == 0 and cpu_roll == 1:
    print("You lost!")
elif int(player_choice) == 1 and cpu_roll == 2:
    print("You lost!")
elif int(player_choice) == 2 and cpu_roll == 0:
    print("You lost!")