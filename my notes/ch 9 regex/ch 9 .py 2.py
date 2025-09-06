# | character is called a pipe. It's used as the alternation operator in regex.
# You can use it anywhere you want to match one of multiple expressions.
# ex. r'Cat|Dog' will match either 'Cat' or 'Dog'.

import re
pattern = re.compile(r'Cat(erpillar|astastrophe|ch|egory)')
match = pattern.search("Catch me if you can.")
print(match.group())
print(match.group(1))

#findall() method will return the strings of EVERY match in the searched string. 
#compared to .search() method which will return a match object of the first matched
# text in a searched string.
#Keep in mind: the .findall() method returns a list of strings AS LONG AS THERE ARE NO GROUPS
# IN THE REGULAR EXPRESSION...

import re
pattern = re.compile(r'\d{3}-\d{3}-\d{4}') #This regex has no groups
print(pattern.findall('Cell: 415-555-9999 Work: 212-555-0000'))

#if there are groups in the regex, .findall() will return a list of tuples.
#each tuple represents a single match
#and the tuple has strings for each group in the regex
import re
pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})') #This regex has groups
print(pattern.findall('Cell: 415-555-9999 Work: 212-555-0000'))

#also, .findall() does not overlap matches...

import re
pattern = re.compile(r'\d{3}')
print(pattern.findall('1234'))
print(pattern.findall('12345'))
print(pattern.findall('123456'))

#QUALIFIER SYNTAX
    #Using Character Classes and Negative Character Classes:
#define a set of characters to match inside square brackets = character class:
# [aeiouAEIOU] will match any vowel, both upper and lower case
# [aeiouAEIOU] = a|e|i|o|u|A|E|I|O|U but easier to type

import re
vowel_pattern = re.compile(r'[aeiouAEIOU]')
vowel_pattern.findall('RoboCop eats BABY FOOD.')
print(vowel_pattern.findall('RoboCop eats BABY FOOD.'))

#Can inclue ranges in classes:
#ex. character class [a-zA-Z0-9] will match all lower/uppercase letters
# and numbers.
# nb. inside square brackets do not nee escape characters like \

#Negative Character class: (will match all characters NOT in the class)
#done by placing a caret ^ just after the class's opening bracket

import re
consonant_pattern = re.compile(r'[^aeiouAEIOU]')
consonant_pattern.findall("RoboCop eats BABY FOOD.")
print(consonant_pattern.findall("RoboCop eats BABY FOOD."))