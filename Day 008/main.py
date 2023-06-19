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


# 85. Caesar Cipher Part 1 - Encryption

# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

# #TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
# def encrypt(plain_text, shift_amount):
#     #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
#     #e.g. 
#     #plain_text = "hello"
#     #shift = 5
#     #cipher_text = "mjqqt"
#     #print output: "The encoded text is mjqqt"

#     ##HINT: How do you get the index of an item in a list:
#     #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

#     ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛
#     cypher_text = ""
#     for letter in (plain_text):
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         if new_position > 25:
#             new_position -= 26
#         cypher_text += alphabet[new_position]
#     print(f"The encoded text is {cypher_text}")

# #TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
# encrypt(plain_text=text, shift_amount=shift)
# -------------------------------------


# 86. Caesar Cipher Part 2 - Decryption

# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         cipher_text += alphabet[new_position]
#     print(f"The encoded text is {cipher_text}")

# #TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
# def decrypt(encrypted_text, shift_amount):
#     #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
#     #e.g. 
#     #cipher_text = "mjqqt"
#     #shift = 5
#     #plain_text = "hello"
#     #print output: "The decoded text is hello"
#     decipher_text = ""
#     for letter in encrypted_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         decipher_text += alphabet[new_position]
#     print(f"The decoded text is {decipher_text}")

# #TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable.
# # Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.

# if direction == "encode":
#     encrypt(plain_text=text, shift_amount=shift)
# elif direction == "decode":
#     decrypt(encrypted_text=text, shift_amount=shift)
# else:
#     print("You have to choose between 'encode' or 'decode' to proceed.")
# -------------------------------------


# 87. Caesar Cipher Part 3 - Reorganising our Code

# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

# #TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 

# def caesar(message=text, shift_amount=shift, cipher_direction=direction):
#     secret_message = ""
 
#     if cipher_direction == "decode":
#         shift_amount *= -1
    
#     for letter in message:
#         position = alphabet.index(letter)            
#         new_position = position + shift_amount
#         secret_message += alphabet[new_position]

#     print(f"The {cipher_direction}d text is: {secret_message}")
         

# #TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
# caesar(message=text, shift_amount=shift, cipher_direction=direction)
# -------------------------------------


# 88. Caesar Cipher Part 4 - User Experience

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):

    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        #TODO-3: What happens if the user enters a number/symbol/space?
        #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
        #e.g. start_text = "meet me at 3"
        #end_text = "•••• •• •• 3"
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    
    print(f"Here's the {cipher_direction}d result: {end_text}")
    

#TODO-1: Import and print the logo from art.py when the program starts.
import art

print(art.logo)


#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 
should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    #TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
    #Try running the program and entering a shift number of 45.
    #Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
    #Hint: Think about how you can use the modulus (%).
    shift = shift % 26
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    result = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n")

    if result == 'no':
        should_continue = False
        print("Goodbye.")
# -------------------------------------