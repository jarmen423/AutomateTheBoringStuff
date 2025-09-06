# Write code that uses it to print the image.
# ..OO.OO..
# .OOOOOOO.
# .OOOOOOO.
# ..OOOOO..
# ...OOO...
# ....O....
# From the provide grid variable 

# Hint: You will need to use a loop in a loop in order to print grid[0][0], 
## then grid[1][0], then grid[2][0], and so on, up to grid[8][0]. 
# This will finish the first row, so then print a newline. 
## Then your program should print grid[0][1], then grid[1][1], then grid[2][1], and so on. 
# The last thing your program will print is grid[8][5].
#Also, remember to pass the end keyword argument to print() if you don’t want a newline 
## printed automatically after each print() call.

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']] 

# This loop within a loop needs to iterate through each item in each list
# The first items in each list should be printed, then the second, and so forth 
for item in range(6): # This keeps track of the item number. == range(len(grid[0]))
    for aList in range(9): # This keeps track of list number. == range(len(grid))
        print(grid[aList][item], end="") # This will print the items on the same line 
    print() # This will end the print statement and start a new line after each particular item number are all printed
        