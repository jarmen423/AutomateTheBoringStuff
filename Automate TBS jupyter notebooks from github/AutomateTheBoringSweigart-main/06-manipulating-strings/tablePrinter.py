# Write a function named printTable() that takes a list of lists of strings and displays it in a well-organized table 
## with each column right-justified. Assume that all the inner lists will contain the same number of strings. 

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(tableData):
    colWidths = [0] * len(tableData) # This line creates a list containing the same number of 0 
                                     ## values as the number of inner lists in tableData
    for num in range(len(tableData)): 
        length = 0
        for item in tableData[num]: 
            if len(item) > length:
                length = len(item)
                colWidths[num] = length 
                #  The above loop converts colWidths to a list containing the values equal to the length of the 
                ## longest string in each list within tableData
    for item in range(len(tableData[0])): # This line loops through each item in the inner lists of tableData
        for aList in range(len(tableData)): # This line loops through the lists in tableData
            print(tableData[aList][item].rjust(colWidths[aList]+2), end="") 
            # The above line prints the current item of the current list of tabledata, right justifying it with
            ## corresponding value from the previously created colWidths list, plus two for readability.
            ## The end argument tells the print statement to continue the print output without a line break 
        print("") # This line adds a line break to the above print statement as each item finishes its loop

printTable(tableData) 