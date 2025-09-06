# Write a function that takes a string and does the same thing as the strip() string method. 
# If no other arguments are passed other than the string to strip, 
## then whitespace characters will be removed from the beginning and end of the string. 
# Otherwise, the characters specified in the second argument to the function will be 
# removed from the string.

import re

def regrexStrip(aStr, char=" "):
    beginRegrex = re.compile(r'^'+char+r'*') # Create Regrex object for beginning of string, char 0 or more times
    endRegrex = re.compile(char+r'*$') # Create Regrex object for char 0 or more times, end of string
    begin = beginRegrex.search(aStr) # Seach for beginRegrex
    end = endRegrex.search(aStr) # Search for endRegrex
    endOfBeginning = begin.span()[-1] # Span method is a a range of indexes in the string, 
                                      ## This is sliced to give me the last index of a char in begin
    beginningOfEnd = end.span()[0] # This will give me the first index of char in end
    return aStr[endOfBeginning:beginningOfEnd] # Means the same as "  Example three  "[2:15] in var3
    


var1 = regrexStrip("Example one")
var2 = regrexStrip(" Example two")
var3 = regrexStrip("  Example three  ")
var4 = regrexStrip("@@@@@Example four@@@@", '@')
print(var1)
print(var2)
print(var3)
print(var4)