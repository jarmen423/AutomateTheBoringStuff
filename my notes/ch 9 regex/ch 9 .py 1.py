#Long way without regex
def is_phone_number(text):
    if len(text) != 12: #phone numbers have exactly 12 characters
        return False
    for i in range(0, 3): #The first 3 characters must be numbers.
        if not text[i].isdecimal():
            return False
    if text[3] != '-': #The 4th character must be a dash.
        return False
    for i in range (4, 7): #The next 3 characters must be numbers.
        if not text[i].isdecimal():
            return False
    for i in range(8, 12): #The next four characters must be numbers. 
        if not text[i].isdecimal():
            return False
    return True

#
message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
    segment = message[i:i+12]
    if is_phone_number(segment):
        print("phone number found:" + segment)
print("Done")

#Regex uses
import re
phone_num_pattern_obj = re.compile(r'\d{3}-\d{3}-\d{4}')
match_obj = phone_num_pattern_obj.search("My number is 415-555-4242.")
print(match_obj.group())


import re
phone_re = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phone_re.search('My number is 415-555-4242.')
mo.group(1) #Returns the first group of the matched text '415'
mo.group(2) #Returns the second group ofthe matched text '555-4242'
mo.group(0) #Returns the full matched text '415-555-4242'
mo.group() #Also returns the ull matched text '415-555-4242'
mo.groups() #Returns all the groups at once ('415', '555-4242')
area_code, main_number = mo.groups()
print(area_code)
print(main_number)

import re
pattern = re.compile(r'(\(\d\d\d\))(\d\d\d-\d\d\d\d)') #If you need to match parentheses in your text; 
mo = pattern.search("My phone number is (415)555-4242.") #escapse the ( ) with back slashes. \( \) will be 
print(mo.group(1))                                      # interpreted as part of the pattern you are matching.
print(mo.group(2))

#In regex, the following characters have special meaning: $()*+-.?[\]^{|}
#If you want to detect these characters as part of your text pattern
#you need to escape them with a backslash: 
# \$ \(\) \* \+ \- \. \? \[\\ \] \^ \{\| \}