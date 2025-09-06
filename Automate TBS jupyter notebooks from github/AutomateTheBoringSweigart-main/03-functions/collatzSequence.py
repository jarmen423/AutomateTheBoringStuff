# This program will ask for a number and print out a collatz seqence for that number,
## then it will terminate. 

number = 0 # This will give us a starting point

while number <= 0: # The number will need to be poistive, which it is currently not
    try:
        number = int(input("Please give me a positive integer. "))
    except ValueError: # If trying to make the input string into an integer causes an error 
                       ## we need to try again
        number = 0

print("Your number is " + str(number)) # Sanitiy check 
print("Now, let's make this number into the number 1 through a Collatz Sequence:")

# This function will perform a collatz sequence;
## if the number is even, divide the number by two 
## if the number is odd, tripple the number and add one
## print each the results of each transformation 
## end when the number == 1 
def collatz():
    global number
    while number != 1:
        if number % 2 == 0: # If number is even
            number //= 2
            print(number)
        elif number % 2 == 1: # If number is odd
            number *= 3
            number += 1
            print(number)
        else:
            print("Oh no, something went very wrong :( ") 
            # I have no idea what would satisfy this condition, 
            ## but it's nice to include anyway
    return number 

# This will actually run the program 
collatz()