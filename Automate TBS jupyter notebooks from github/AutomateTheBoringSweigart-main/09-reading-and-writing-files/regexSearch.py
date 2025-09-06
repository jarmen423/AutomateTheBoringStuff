# This program opens all .txt files in a folder and searches for any line that matches 
## a user-supplied regular expression. The results should be printed to the screen.

from pathlib import Path
import pyinputplus as pyip

valid = False
while valid == False:
    userPath = Path(pyip.inputFilepath("Folder name (include absolute path): ", mustExist=True))
    if userPath.is_absolute() == False:
        print("Please rewrite you folder name so it includes the absolute path.")
    elif userPath.exists() == False:
        print("Note, this path does not appear to exist, please try again.")
    elif userPath.is_dir() == False: 
        print("You have not entered the path to a folder, please try again")
    else:
        valid = True
# The above block asks for a user given directory, including the absolute path, and validates the input

userRegex = pyip.inputRegexStr("Search for (regex compatible): ")
# The above line takes a user input for a regex string. 
## Note: Because regex is built into pyinputplus this program does not need to import re

for path_txt in userPath.glob('*.txt'):
    textFile = open(path_txt)
    inFile = textFile.read()
    matches = userRegex.findall(inFile)
    textFile.close()
    print("In file: {}\n{}".format(path_txt, matches))
# The above block iterates through all files in the userPath that end in .txt 
## then searches within those files for strings that match the userregex 
## printing the path/file and the the matched strings
