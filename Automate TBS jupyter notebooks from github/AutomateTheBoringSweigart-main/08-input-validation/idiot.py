# This is a simple program that does the following:
## Ask the user if they’d like to know how to keep an idiot busy for hours.
## If the user answers no, quit.
## If the user answers yes, go to Step 1.

import pyinputplus as pyip

while True: # Continues to run loop until a break statement 
    prompt = 'Want to know how to keep an idiot busy for hours?\n'
    response = pyip.inputYesNo(prompt)
    if response == 'no': # Nothing besides input == "n" or "no" will satisfy pyip.inputYesNo() 
                         # and this if statement
        print('Thank you. Have a nice day.')
        break
