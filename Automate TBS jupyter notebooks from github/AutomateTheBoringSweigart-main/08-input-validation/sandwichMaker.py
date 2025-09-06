# Write a program that asks users for their sandwich preferences. 
## The program should use PyInputPlus to ensure that they enter valid input.
## Come up with prices for each of these options, 
## and have your program display a total cost after the user enters their selection.

import pyinputplus as pyip

print("Let's make your sandwich. Select the number of each item you want.") 
print("If you screw up, just go to the end and start again.") 
# There's probably a way to include a 'go back to last question' option, but this project didn't require one

options = [] # This will track choices in string form for printing later on
price = 200 
# Using a float gave me some stranging rounding errors, so this price will be in pennies
## I start the price at two dollars as a minimum for default options, and add to price only when required
bread = pyip.inputMenu(["wheat ($1.00)" , "white ($1.00)", "sourdough ($1.10)"], numbered=True)
options.append(bread)
if bread == "sourdough ($1.10)": 
    price += 10
protien = pyip.inputMenu(["chicken ($1.00)", "turkey ($1.00)", "ham ($1.10)", "tofu ($1.20)"], numbered=True)
options.append(protien)
if protien == "ham ($1.10)":
    price += 10
elif protien == "tofu ($1.20)":
    price += 20
cheese = pyip.inputYesNo(prompt="Do you want cheese ($0.50)? 1: yes 2: no\n", yesVal=1, noVal=2) 
# I want to keep 'choose the number' consistency, so yesVal and noVal are changed
if cheese == "1":
    price += 50
    cheeseChoise = pyip.inputMenu(["cheddar ($0.50)", "swiss ($0.50)", "mozzarella ($0.50)"], numbered=True)
    options.append(cheeseChoise)
    # pyip.inputYesNo() doesn't choose the cheese choice, so that needs to be chosen sperately 
mayo = pyip.inputYesNo(prompt="Do you want mayonnaise ($0.05)? 1: yes 2: no\n", yesVal=1, noVal=2)
if mayo == "1":
    price += 5
    options.append("mayonnaise ($0.05)")
mustard = pyip.inputYesNo(prompt="Do you want mustard ($0.05)? 1: yes 2: no\n", yesVal=1, noVal=2)
if mustard == "1":
    price += 5
    options.append("mustard ($0.05)")
lettuce = pyip.inputYesNo(prompt="Do you want lettuce ($0.05)? 1: yes 2: no\n", yesVal=1, noVal=2)
if lettuce == "1":
    price += 5
    options.append("lettuce ($0.05)")
tomato = pyip.inputYesNo(prompt="Do you want tomato ($0.05)? 1: yes 2: no\n", yesVal=1, noVal=2)
if tomato == "1":
    price += 5
    options.append("tomato ($0.05)")

print("Your order is: ") # Display all chosen options from options list
for i in options:
    print(i)
print("Price: " + "$" + str(price)[0] + "." + str(price)[1:]) 
# Display price integer with proper format
## This would need to be reformatted if the price could exceed $9.99 due to str(price)[1:]
confirmation = pyip.inputMenu(["Yes.", "No, start again.", "Nevermind."], prompt="Is this correct?\n", numbered=True)
# There were no requirements for a confirmation screen, but it might start with something like what is above 
## before more code was added to do something with confirmation 