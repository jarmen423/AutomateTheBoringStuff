# Write a function that uses regular expressions to make sure the password string it is passed is strong.
# A strong password is defined as one that is at least eight characters long, 
## contains both uppercase and lowercase characters, and has at least one digit. 
# You may need to test the string against multiple regex patterns to validate its strength.

#! python 3

import pyperclip, re

def passwordCheck(aStr):
    validPassword = True # Initializing variable to check later 

    lengthRegrex = re.compile(r'.{8,}') # Regrex object of any string at least 8 characters long 
    if lengthRegrex.search(aStr) == None: # Search within aStr 
        print("Not long enough")
        validPassword = False
    lowerRegrex = re.compile(r'[a-z]+') # Regrex object of at least one lowercase letter 
    if lowerRegrex.search(aStr) == None: # Search within aStr 
        print("Needs a lowercase letter")
        validPassword = False
    upperRegrex = re.compile(r'[A-Z]+') # Regrex object of at least one uppercase letter 
    if upperRegrex.search(aStr) == None: # Search within aStr  
        print("Needs an uppercase letter")
        validPassword = False
    numRegrex = re.compile(r'\d+') # Regrex object of at least one number
    if numRegrex.search(aStr) == None: # Search within aStr 
        print("Needs a number")
        validPassword = False
    specCharRegrex = re.compile(r'\W+') # Regrex object of at least one character that is not a number or letter 
    if specCharRegrex.search(aStr) == None: # Search within aStr 
        print("Needs special character, such as : `~!@#$%^&*()_-=+,<.>/?;:\'\"[{]}|\\")
        validPassword = False
    if validPassword == True: # If no checks find False
        print("Password is strong (enough)!")

text = str(pyperclip.paste()) # Save whatever is on computer clipboard to text variable
passwordCheck(text) 