# Write a program to find out how often a streak of six heads or a streak of six tails 
## comes up in a randomly generated list of heads and tails. 
# Your program breaks up the experiment into two parts: 
## the first part generates a list of randomly selected 'heads' and 'tails' values, 
## and the second part checks if there is a streak in it. 
# Put all of this code in a loop that repeats the experiment 10,000 times 
## so we can find out what percentage of the coin flips contains a streak of six heads or tails in a row. 
# As a hint, the function call random.randint(0, 1) 
## will return a 0 value 50% of the time and a 1 value the other 50% of the time.

import random 

numberOfStreaks = 0 # This will keep a running tally of each flip-set that contains at least one streak 
for experimentNumber in range(10000): # This simulation will be run 10,000 times
    # Code that creates a list of 100 'heads' or 'tails' values. 
    flipList = [] 
    for i in range(100): # This generates a list of 100 coin flips 
        flip = random.randint(0, 1)
        if flip == 0: # While 0/1 is mathmatically fine, this will make the coin flips explicitly Heads/Tails 
            flipList.append("Heads") 
        else:
            flipList.append(("Tails")) 

    # Code that checks if there is a streak of 6 heads or tails in a row.
    counter = 0 # A starting place for counting streaks 
    sucess = False # A starting place for deciding if the flip-set contains at least one streak 
    for number, flip in enumerate(flipList):
        if number == 0: # This skips checking the first item in the flip set against the previous flip 
            pass
        elif flip == flipList[number-1]: # This checks the item in the flip set against the previous flip 
            counter += 1 
            if counter == 6: # If a streak of 6 comes up, the condition is satisfied and there is no longer any need 
                             ## to move through this flip-set 
                sucess = True
                break
        elif flip != flipList[number-1]: # If the check is not the same as the previous, the counter needs to be reset 
            counter = 0
    if sucess == True: # After the break, or after the last item in the flip set, this will modify the running tally 
        numberOfStreaks += 1

# This statement gives the number of streaks that met the sucess condition (>= 6 Heads or Tails in a row, at least once)
# divided by 100, and represents that quotient as a percentage 
print('Chance of streak: %s%%' % (numberOfStreaks / 100))
