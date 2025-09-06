# This program finds all files with a given prefix in a single folder and locates any gaps in the numbering 
## (such as if there is a spam001.txt and spam003.txt but no spam002.txt). 
## Have the program rename all the later files to close this gap.

import shutil, re, os

def gapFiller(sourcePath, prefix):
    filenames = os.listdir(sourcePath)
    list.sort(filenames)
    # The above block gets a list of filenames from the sourcePath folder and sorts them alphabetically
    matchingList = []
    for string in filenames:
        if prefix in string:
            matchingList.append(string)
    # The above block creates a new list containing only the files containing the prefix string
    numberRegex = re.compile(prefix + r'(\d+)(\..+$)')
    for i in range(len(matchingList)):
        numSearch = numberRegex.search(matchingList[i])
        if i+1 != int(numSearch[1]):
            shutil.copy(sourcePath+'/'+matchingList[i], sourcePath+'/'+prefix+'0'+str(i+1)+numSearch[2])
    # The above block finds the numbers following the prefixes in the filenames from matchingList, 
    ## iterates through these filenames and changing the number in the filename if the number 
    ## does not match the iterateion

gapFiller('/Users/trevorcline/code/AutomateTheBoringSweigart/10-organizing-files/folder/subfolder1', 'jpg_file')