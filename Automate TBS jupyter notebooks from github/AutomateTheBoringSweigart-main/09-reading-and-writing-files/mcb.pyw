#! python3 
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.

# A newer version of mclip.py from ../06-manipulating-strings
# The user will now be able to save new strings to load to the clipboard without having to modify the source code. 
# The .pyw extension means that Python won’t show a Terminal window when it runs this program.

# Here’s what the program does:
## The command line argument for the keyword is checked.
## If the argument is save, then the clipboard contents are saved to the keyword.
## If the argument is list, then all the keywords are copied to the clipboard.
## Otherwise, the text for the keyword is copied to the clipboard.
# This means the code will need to do the following:
## Read the command line arguments from sys.argv.
## Read and write to the clipboard.
## Save and load to a shelf file.

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb') # This file is created with this run, and is saved in the cwd 

# Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    # List keywords and load content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()

