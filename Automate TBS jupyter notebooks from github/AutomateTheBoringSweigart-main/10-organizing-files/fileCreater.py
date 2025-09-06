# Creates example folders/files to use in other projects


from pathlib import Path
import os 

os.chdir('/Users/trevorcline/code/AutomateTheBoringSweigart/10-organizing-files/')
print(Path.cwd())
# This block sets the working directory to what is printed above, 
# then prints the current working directory for comfirmation 


os.makedirs('./folder')
for i in range(1,3):
    os.makedirs('./folder' + '/subfolder' + str(i))
    for fileType in ['.txt', '.pdf', '.jpg']:
        for ii in range(1,9):
            if ii == 6: # To not skip number 6's, delete this if statement
                continue
            open('./folder' + '/subfolder' + str(i) + '/' + fileType[1:] + '_file' + str(ii).rjust(2,'0') + fileType, 'w')
# The above block generates a one new folder containing two subfolders, 
## each of which contain seven .txt, .pdf, .jpg files, with but the names ending in 6 will be skipped
# Note, this will not work if the folders already exist 

