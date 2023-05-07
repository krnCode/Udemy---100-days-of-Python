# Course Project - Tip Calculator
# https://replit.com/@appbrewery/tip-calculator-start?v=1

# If the bill was $150.00, split between 5 people, with 12% tip. 

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Write your code below this line 👇

# Greetings message
startMessage = 'Welcome to the tip calculator!'

print(startMessage)


# Get input from the user
inputBill = input('What was the total bill? ')
inputTip = input('How much tip would you like to give? 10, 12 or 15? ')
inputPeople = input('How many people to split the bill? ')


# Convert inputs into int/float datatypes
convertedBill = float(inputBill)
convertedTip = int(inputTip)
convertedPeople = int(inputPeople)


# Calculations
billCalculation = (convertedBill / convertedPeople)
tipCalculation = billCalculation * ((convertedTip / 100) + 1)


# Create variable to format 2 decimal numbers
finalAmount = "{:.2f}".format(tipCalculation)


# Show result to user
print(f"Each person should pay: ${finalAmount}")



# https://replit.com/@appbrewery/tip-calculator-end