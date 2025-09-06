#! python3

# Write a regular expression that can detect dates in the DD/MM/YYYY format. 
## Assume that the days range from 01 to 31, the months range from 01 to 12, and the years range 
## from 1000 to 2999. Note that if the day or month is a single digit, it’ll have a leading zero.

# The regular expression doesn’t have to detect correct days for each month or for leap years; 
## it will accept nonexistent dates like 31/02/2020 or 31/04/2021. 
# Then store these strings into variables named month, day, and year, 
## and write additional code that can detect if it is a valid date. 
# April(4), June(6), September(9), and November(11) have 30 days, February has 28 days, 
## and the rest of the months have 31 days.  February has 29 days in leap years. 
# Leap years are every year evenly divisible by 4, except for years evenly divisible by 100, 
## unless the year is also evenly divisible by 400.

import pyperclip, re

text = str(pyperclip.paste()) # Save whatever is on computer clipboard to text variable
    
dateRegex = re.compile(r'(\d+)/(\d+)/(\d+)') # Object for "number / number / number"
                                             ## with each number in its own group
allDates = dateRegex.findall(text) # This will find all date formats as a list of tuples [(day/month/year)]

validDates = [] # Valid dates will fill this list
for aTuple in allDates: 
    dateValid = True # Instantiate to reference later 
    shortMonths = [2, 4, 6, 9, 11] # Months: Feb, Mar, June, Sep, Nov
    day, month, year = aTuple[0], aTuple[1], aTuple[2] # Creates an independant variable with all groups of tuple
    if int(month) >12 or int(month) <1: # Is month a valid number? 
        dateValid = False
    if int(day) >31 or int(day) <1: # Is day a valid number? 
        dateValid = False
    if int(day) == 31 and int(month) in shortMonths: # Is day addionally valid in the context of Month?
        dateValid = False
    if int(day) >29 and int(month) == 2: # Is day valid in the context of February? 
        dateValid = False 
    if int(day) == 29 and int(month) == 2: # Is it a leap year (year divisible by 4 but not 100 unless also 400)? 
        if int(year) % 4 == 0: 
            if int(year) % 400 == 0:
                pass
            elif int(year) % 100 == 0:
                dateValid = False
            else:
                pass
        else:
            dateValid = False
    if dateValid == True: # If no checks find False 
        validDates.append([day, month, year]) 
            

datesString = "" # This string will be built a new string from the contents of validDates
for aList in validDates:
    for item in aList:
        datesString += item 
        if item != aList[-1]: # Add a slah or a space in respective place
            datesString += "/"
        else: 
            datesString += " "



pyperclip.copy("Valid dates: " + datesString) # Past new string 