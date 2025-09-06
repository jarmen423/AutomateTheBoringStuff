# Find the bug.
# Hint: Look at the output.

import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s -  %(levelname)s -  %(message)s')
# logging.disable(logging.CRITICAL)
## The above line is commented to allow debugging print statements. 
## Uncommenting that line will remove debug excess output for the user
logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s)'  % (n))
    total = 1
    for i in range(1, n + 1): # This line was changed to make this program work 
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(%s)'  % (n))
    return total

print(factorial(5))
logging.debug('End of program')