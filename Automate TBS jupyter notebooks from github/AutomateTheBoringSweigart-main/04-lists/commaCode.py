# Write a function that takes a list value as an argument and returns a 
## string with all the items separated by a comma and a space, 
## with and inserted before the last item. 

def commaString(aList):
    newString = "" # This string will be built and returned by this function
    for i in range(len(aList)): # Each item in the given list must be iterated 
        if i != (len(aList)-1): # This will add the comma and space to each item in the list
            newString = newString + aList[i] + ", "
        else:  # This condition will only be satisfied on the lat item in the list, adding the "and "
            newString = newString + "and " + aList[i]
    return newString    

# These statements check the function
print(commaString(['apples', 'bananas', 'tofu', 'cats']))
print(commaString([]))