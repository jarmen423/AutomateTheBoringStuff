# Write a function named isValidChessBoard() that takes a dictionary argument 
## and returns True or False depending on if the board is valid.
# A valid board will have exactly one black king and exactly one white king. 
# Each player can only have at most 16 pieces, at most 8 pawns, and all pieces must be on a valid space 
## from '1a' to '8h'; that is, a piece can’t be on space '9z'. 
# The piece names begin with either a 'w' or 'b' to represent white or black, 
## followed by 'pawn', 'knight', 'bishop', 'rook', 'queen', or 'king'. 
# This function should detect when a bug has resulted in an improper chess board.

# The boards being tested; the function is below
validBoard = {'1a': 'wrook','2a': 'wpawn','3a': '','4a': '',
'5a': '','6a': '','7a':'bpawn','8a': 'brook',
'1b': 'wknight','2b': 'wpawn','3b': '','4b':'',
'5b': '','6b': '','7b': 'bpawn','8b': 'bknight',
'1c': 'wbishop','2c': 'wpawn','3c': '','4c': '',
'5c': '','6c': '','7c': 'bpawn','8c':'bbishop',
'1d': 'wqueen', '2d': 'wpawn', '3d': '', '4d': '',
'5d': '', '6d': '', '7d': 'bpawn', '8d': 'bqueen',
'1e': 'wking','2e': 'wpawn','3e': '','4e': '',
'5e': '','6e': '','7e': 'bpawn','8e': 'bking',
'1f': 'wbishop','2f': 'wpawn','3f': '','4f': '',
'5f': '','6f': '','7f': 'bpawn','8f': 'bbishop',
'1g': 'wknight','2g': 'wpawn','3g': '','4g': '',
'5g': '','6g': '','7g': 'bpawn','8g': 'bknight',
'1h': 'wrook','2h': 'wpawn','3h': '','4h': '',
'5h': '','6h': '','7h': 'bpawn','8h': 'brook',}

noWhiteKingBoard = {'1a': 'wrook','2a': 'wpawn','3a': '','4a': '',
'5a': '','6a': '','7a':'bpawn','8a': 'brook',
'1b': 'wknight','2b': 'wpawn','3b': '','4b':'',
'5b': '','6b': '','7b': 'bpawn','8b': 'bknight',
'1c': 'wbishop','2c': 'wpawn','3c': '','4c': '',
'5c': '','6c': '','7c': 'bpawn','8c':'bbishop',
'1d': 'wqueen', '2d': 'wpawn', '3d': '', '4d': '',
'5d': '', '6d': '', '7d': 'bpawn', '8d': 'bqueen',
'1e': '','2e': 'wpawn','3e': '','4e': '',
'5e': '','6e': '','7e': 'bpawn','8e': 'bking',
'1f': 'wbishop','2f': 'wpawn','3f': '','4f': '',
'5f': '','6f': '','7f': 'bpawn','8f': 'bbishop',
'1g': 'wknight','2g': 'wpawn','3g': '','4g': '',
'5g': '','6g': '','7g': 'bpawn','8g': 'bknight',
'1h': 'wrook','2h': 'wpawn','3h': '','4h': '',
'5h': '','6h': '','7h': 'bpawn','8h': 'brook',}

tooManyPiecesBoard = {'1a': 'wrook','2a': 'wpawn','3a': '','4a': '',
'5a': '','6a': '','7a':'bpawn','8a': 'brook',
'1b': 'wknight','2b': 'wpawn','3b': '','4b':'',
'5b': '','6b': '','7b': 'bpawn','8b': 'bknight',
'1c': 'wbishop','2c': 'wpawn','3c': '','4c': '',
'5c': 'wpawn','6c': '','7c': 'bpawn','8c':'bbishop',
'1d': 'wqueen', '2d': 'wpawn', '3d': '', '4d': '',
'5d': '', '6d': '', '7d': 'bpawn', '8d': 'bqueen',
'1e': 'wking','2e': 'wpawn','3e': '','4e': '',
'5e': '','6e': '','7e': 'bpawn','8e': 'bking',
'1f': 'wbishop','2f': 'wpawn','3f': '','4f': '',
'5f': '','6f': '','7f': 'bpawn','8f': 'bbishop',
'1g': 'wknight','2g': 'wpawn','3g': '','4g': '',
'5g': '','6g': '','7g': 'bpawn','8g': 'bknight',
'1h': 'wrook','2h': 'wpawn','3h': '','4h': '',
'5h': '','6h': '','7h': 'bpawn','8h': 'brook',}

tooManyPawnsBoard = {'1a': 'wrook','2a': 'wpawn','3a': '','4a': '',
'5a': '','6a': '','7a':'bpawn','8a': 'brook',
'1b': 'wknight','2b': 'wpawn','3b': '','4b':'',
'5b': '','6b': '','7b': 'bpawn','8b': 'bknight',
'1c': 'wpawn','2c': 'wpawn','3c': '','4c': '',
'5c': '','6c': '','7c': 'bpawn','8c':'bbishop',
'1d': 'wqueen', '2d': 'wpawn', '3d': '', '4d': '',
'5d': '', '6d': '', '7d': 'bpawn', '8d': 'bqueen',
'1e': 'wking','2e': 'wpawn','3e': '','4e': '',
'5e': '','6e': '','7e': 'bpawn','8e': 'bking',
'1f': 'wbishop','2f': 'wpawn','3f': '','4f': '',
'5f': '','6f': '','7f': 'bpawn','8f': 'bbishop',
'1g': 'wknight','2g': 'wpawn','3g': '','4g': '',
'5g': '','6g': '','7g': 'bpawn','8g': 'bknight',
'1h': 'wrook','2h': 'wpawn','3h': '','4h': '',
'5h': '','6h': '','7h': 'bpawn','8h': 'brook',}

cheatingPawnBoard = {'1a': 'wrook','2a': 'wpawn','3a': '','4a': '',
'5a': '','6a': '','7a':'bpawn','8a': 'brook',
'1b': 'wknight','2b': 'wpawn','3b': '','4b':'',
'5b': '','6b': '','7b': 'bpawn','8b': 'bknight',
'1c': 'wpawn','2c': 'wbishop','3c': '','4c': '',
'5c': '','6c': '','7c': 'bpawn','8c':'bbishop',
'1d': 'wqueen', '2d': 'wpawn', '3d': '', '4d': '',
'5d': '', '6d': '', '7d': 'bpawn', '8d': 'bqueen',
'1e': 'wking','2e': 'wpawn','3e': '','4e': '',
'5e': '','6e': '','7e': 'bpawn','8e': 'bking',
'1f': 'wbishop','2f': 'wpawn','3f': '','4f': '',
'5f': '','6f': '','7f': 'bpawn','8f': 'bbishop',
'1g': 'wknight','2g': 'wpawn','3g': '','4g': '',
'5g': '','6g': '','7g': 'bpawn','8g': 'bknight',
'1h': 'wrook','2h': 'wpawn','3h': '','4h': '',
'5h': '','6h': '','7h': 'bpawn','8h': 'brook',}



# The arguement board must be a dictionary, such as the boards above
def isValidChessBoard(board):
    # These values and touples of values will be referenced later
    blackPieces = 0
    whitePieces = 0
    wpawn = 0
    bpawn = 0
    letterAxis = ('a','b','c','d','e','f','g','h')
    pieceColor = ('b','w')
    pieceType = ('pawn','knight','bishop','rook','queen','king')
    
    # Piece names begin with 'w' or 'b'
    for i in board.values(): # This will only check the values of the board dictionary 
        if i == "": # If I tried to slice a string (as in i[0]) that was empty ( as in "") 
                    ## I would get an error
            pass # So I must first avoid slicing empty strings 
        elif i[0] not in pieceColor: # This will test the first letter in the value string
            print("Pieces not all black or white") # Output tells the reason for invalidation of board
            return False # All invalid boards will return False

    # Piece names must follow with 'pawn', 'knight', 'bishop', 'rook', 'queen', 'king'
    for i in board.values(): 
        if i == "": # This is the same logic as above, will be used again as well
            pass
        elif i[1:] not in pieceType: # This will test all other letters not including the first letter
                                     ## the of value string
            print("Pieces contain invalid names")
            return False

    # All pieces must be on valid space from '1a' to '8h'
    for i in board.keys(): # This will only check the keys of the board dictionary 
        if int(i[0]) > 8: # The key string must start with a number under 8 
            print("Board has incorrect horizontal dimentions")
            return False
        if i[1] not in letterAxis: # The key string must end with a letter from a-h
            print("Board has incorrect vertical dimentions")
            return False

    # One black king and one white king
    if 'bking' not in board.values(): 
        print("No black king")
        return False
    if 'wking' not in board.values():
        print("No white king")
        return False
    
    # Each player has <= 16 pieces
    for i in board.values():
        if i == "": 
            pass
        elif i[0] == 'b':
            blackPieces+=1
        elif i[0] == 'w':
            whitePieces+=1
        if whitePieces > 16 or blackPieces > 16:
            print("Too many pieces")
            return False

    # Each player has <= 8 pawns
    for i in board.values():
        if i == 'wpawn':
            wpawn+=1
        elif i == 'bpawn':
            bpawn+=1
        if wpawn > 8 or bpawn > 8:
            print("Too many pawns")
            return False

    # Pawns cannot be on top or bottom row 
    for k, v in board.items(): # This will check both keys and values 
        if v == "":
            pass 
        elif v[1:] != "pawn": # this will isolate the checked values to only those ending with "pawn"
            pass
        elif k[0] == "1" or k[0] == "8": 
            print("Pawn on invalid square")
            return False
        
    # There are several types of invalid chess boards that would still pass this function, however this code
    ## is already long and futher checks (e.g., making sure no more than one king is on each side, making sure
    ## that if there is more than one white queen that it had been promoted from a pawn, making sure that 
    ## only one pawn is on a roaw unless a piece is missing such that the pawn changed rows capturing it, etc.)
    ## would be a real pain in the side to continue create for a code that is only meant for practice. 

    print("No board errors detected") # This line can only be ran if the function did not return previously
    return True # If no validation checks failed, return true


print("validBoard is " + str(isValidChessBoard(validBoard)))
print("noWhiteKingBoard is " + str(isValidChessBoard(noWhiteKingBoard)))
print("tooManyPiecesBoard is " + str(isValidChessBoard(tooManyPiecesBoard)))
print("tooManyPawnsBoard is " + str(isValidChessBoard(tooManyPawnsBoard)))
print("cheatingPawnBoard is " + str(isValidChessBoard(cheatingPawnBoard)))