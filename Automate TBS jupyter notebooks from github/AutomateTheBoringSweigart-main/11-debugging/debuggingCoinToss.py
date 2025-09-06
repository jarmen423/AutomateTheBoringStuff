# The following program is meant to be a simple coin toss guessing game. 
# The player gets two guesses (it’s an easy game). 
## However, the program has several bugs in it. Run through the program a few times 
## to find the bugs that keep the program from working correctly.


import random
def buggyCoinToss():
    guess = ''
    while guess not in ('heads', 'tails'):
        print('Guess the coin toss! Enter heads or tails:')
        guess = input()
    toss = random.randint(0, 1) # 0 is tails, 1 is heads
    if toss == guess:
        print('You got it!')
    else:
        print('Nope! Guess again!')
        guesss = input()
        if toss == guess:
            print('You got it!')
        else:
            print('Nope. You are really bad at this game.')


def betterCoinToss(): # This is the same as above, but changes are made and commented
    guess = ''
    while guess not in ('heads', 'tails'):
        print('Guess the coin toss! Enter heads or tails:')
        guess = input()
    toss = random.randint(0, 1) # 0 is tails, 1 is heads
    if toss == (guess == 'heads'): 
        # The above line was changed 
        ## instead of checking if toss (either 1 or 0) == guess (either 'heads' or 'tails'),
        ## this checks if toss == (1 or 0) == (True or False)
        ## This works because 1 == True and 0 == False
        print('You got it!')
    else:
        print('Nope! Guess again!')
        while guess not in ('heads', 'tails'):
            print('Guess the coin toss! Enter heads or tails:')
            guess = input() # This also was changed to remove an extra "s" in the variable guess
        # The above line was changed to reintroduce the while loop to check 
        if toss == (guess == 'heads'): # See same line above
            print('You got it!')
        else:
            print('Nope. You are really bad at this game.')

buggyCoinToss()
betterCoinToss()
