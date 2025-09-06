# Project: Extend the multi-clipboard program so that it has a delete <keyword> command line argument 
## that will delete a keyword from the shelf. Then add a delete command line argument that will delete all keywords.

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb') # This file is created with this run, and is saved in the cwd 

# Save clipboard content.
if len(sys.argv) == 3:
    if sys.argv[1].lower() == 'save':
        mcbShelf[sys.argv[2]] = pyperclip.paste()
    elif sys.argv[1].lower() == 'delete':
        if sys.argv[2] in mcbShelf:
            del mcbShelf[sys.argv[2]]
        else:
            print(str(mcbShelf[sys.argv[2]]) + " cannot be deleted because it is not saved")
elif len(sys.argv) == 2:
    # List keywords and load content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
    elif sys.argv[1].lower() == 'delete-all':
        mcbShelf.clear()

mcbShelf.close()