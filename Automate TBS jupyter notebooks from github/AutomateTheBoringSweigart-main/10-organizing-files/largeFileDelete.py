# This program walks through a folder tree and 
## searches for exceptionally large files or folders—say, ones that have a file size of more than 1000B. 
# Print these files with their absolute path to the screen so that the code may be changed to delete these files.

import os

def findAndDelete(sourcePath):
    for foldername, subfolders, filenames in os.walk(sourcePath):
        for filename in filenames:
            if os.path.getsize(foldername + "/" + filename) > 1000:
                print()
                print(foldername + "/" + filename)
                print(str(os.path.getsize(foldername + "/" + filename)) + " Bytes")
                print()
# This function walks through the folders and files in the sourcePath directory, 
## and if the files are over 1000 bites the path+file with file size is printed with blank space before/after

findAndDelete('/Users/trevorcline/code/AutomateTheBoringSweigart/10-organizing-files')
