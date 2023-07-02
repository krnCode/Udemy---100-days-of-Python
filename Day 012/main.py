# 116. Namespaces: Local vs. Global Scope

################### Scope ####################

# enemies = 1


# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function: {enemies}")


# increase_enemies()
# print(f"enemies outside function: {enemies}")


# Local Scope


# def drink_potion():
#     potion_strenght = 2
#     print(potion_strenght)


# Global Scope

# player_health = 10


# def game():
#     def drink_potion():
#         potion_strenght = 2
#         print(player_health)

#     drink_potion()


# print(player_health)
# -------------------------------------


# 117. Does Python Have Block Scope?


# def game():
#     def drink_potion():
#         potion_strenght = 2
#         print(player_health)

#     drink_potion()


# print(player_health)

# There is no Block Scope

# if 3 > 2:
#     a_variable = 10

# game_level = 3


# def create_enemy():
#     enemies = ["Skeleton", "Zombie", "Alien"]
#     if game_level < 5:
#         new_enemy = enemies[0]


# print(new_enemy)
# -------------------------------------


# 118. How to Modify a Global Variable

# Modifying Global Scope

# enemies = 1


# def increase_enemies():
#     # global enemies
#     print(f"enemies inside function: {enemies}")
#     return enemies + 1


# enemies = increase_enemies()
# print(f"enemies outside function: {enemies}")
# -------------------------------------


# 119. Python Constants and Global Scope

# Global Constants

# PI = 3.14159
# URL = "https://www.google.com"
# TWITTER_HANDLE = "@yu_angela"
# -------------------------------------
