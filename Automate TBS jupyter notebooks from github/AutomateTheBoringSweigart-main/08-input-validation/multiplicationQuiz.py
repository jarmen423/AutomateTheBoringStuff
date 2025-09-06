# This is a program creates a timed math quiz 
## by posing 10 multiplication problems to the user, where the valid input is the problem’s correct answer. 

import pyinputplus as pyip
import random, time

numberOfQuestions = 10
correctAnswers = 0
for questionNumber in range(numberOfQuestions):
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    prompt = '#%s: %s x %s = ' % (questionNumber+1, num1, num2) 
    # Two random numbers are chosen and given as a prompt above
    try:
        # Right answers are handled by allowRegexes.
        # Wrong answers are handled by blockRegexes, with a custom message.
        pyip.inputStr(prompt, allowRegexes=['^%s$' % (num1 * num2)],
                              blockRegexes=[('.*', 'Incorrect!')],
                              timeout=8, limit=3)
    except pyip.TimeoutException:
        print('Answered too slow! (8 seconds)')
    except pyip.RetryLimitException:
        print('Out of tries! (3)')
    else:
        # This block runs if no exceptions were raised in the try block.
        print('Correct!')
        correctAnswers += 1
    time.sleep(1) # Brief pause to let user see the result.
print('Score: %s / %s' % (correctAnswers, numberOfQuestions))