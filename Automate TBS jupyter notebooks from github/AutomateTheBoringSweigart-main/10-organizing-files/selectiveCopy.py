# Write a program that walks through a folder tree and searches for files with a certain file extension 
## (such as .pdf or .jpg). Copy these files from whatever location they are in to a new folder.

import shutil, os, re
from pathlib import Path

os.chdir('/Users/trevorcline/code/AutomateTheBoringSweigart/10-organizing-files/')
print(Path.cwd())
# The above block changes the current working directory and then prints the cwd

def selectCopy(sourcePath):
    fileRegex = re.compile(r'.+\.(pdf|jpg)$')
    shutil.copytree(sourcePath, './copy_folder')
    for foldername, subfolders, filenames in os.walk('./copy_folder'):
        for filename in filenames:
            fileToDel = fileRegex.search(filename)
            if fileToDel == None:
                os.unlink(foldername + "/" + filename)
# This function copies all subfolders and files from the sourcePath directory into a newly created 
## "copy_folder" directory within the cwd. The files that do not end with a .pdf or .jpg are then 
## deleted from the "copy_folder" directory

selectCopy('./folder')