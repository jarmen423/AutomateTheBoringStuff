# This program creates a Mad Libs that reads in madLib.txt file 
## and lets the user add their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB appears

# Read in madLib.txt
# Create new text file madLib_complete.txt
# Iterate through in search of wordtypes ['ADJECTIVE', 'NOUN', 'ADVERB', 'VERB']
# Recieve input while displaying "Enter a _:" 
# Replace wordtype in madLib_complete.txt with replacement word

import re

# This code uses a relative path and must be run from the directory housing the AutomateTheBoringSweigart directory

sentenceFile = open("./AutomateTheBoringSweigart/09-reading-and-writing-files/madLib.txt") 
sentence = sentenceFile.read()
sentenceFile.close()
# The above block opens the madLib.txt file and saves the string to the variable sentence, then closes the file

wordsAndPunct = re.compile(r'(\w+)(\W+)').findall(sentence)
# The above line uses re to make a list of two-item touples from the sentence variable
## each touple contains the words from sentence in index 0 and the punctuation and space in index 1

newStentence = ""
wordTypes = ['ADJECTIVE', 'NOUN', 'ADVERB', 'VERB']
for i in wordsAndPunct:
    if i[0] in wordTypes:
        replacement = input("Enter a(n) {}: ".format(i[0]))
        newStentence += replacement + i[1]
    else:
        newStentence += i[0] + i[1]
# The above block iterates through every touple in wordsAndPunct to create newSentence,
## the word is replaced with user input if it is in wordTypes, the word and punctuation is then added 

outputFile = open("./AutomateTheBoringSweigart/09-reading-and-writing-files/madLib_complete.txt", "w")
outputFile.write(newStentence)
outputFile.close()
# The above block creates a new file and fills it with the string from newSentence
