#imports random integer's
from random import randint

#makes an empty list called bored
board = []

for x in range(5):
    board.append(["O"] * 5)

#defines the function for battle
def print_board(board):
    #for loop to join the row's in the empty list board
    for row in board:
        print " ".join(row)

print "Let's play Battleship!"

#prints out the board
print_board(board)

#function returns a random integer less than the length of the board
def random_row(board):
    return randint(0, len(board) - 1)

#function returns a random integer less than the length of the board
def random_col(board):
    return randint(0, len(board[0]) - 1)

#sets ship_row equal and column to random rows
ship_row = random_row(board)
ship_col = random_col(board)

#prints out the board
print ship_row
print ship_col

# Everything from here on should go in your for loop!
# Be sure to indent four spaces!
for turn in range(4):
    print "Turn", turn + 1
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))
	#if loop that lets you win if you guess the correct column and row    
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
        break

	# else loop if you guess wrong
    else:

	# allows you to guess bewteen 0-4 no more no less
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops, that's not even in the ocean."
	
	#if you guess x it will say you already guess the value
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        else:

		# loop for if you missed the ship
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"

		#quits the game if you lose
        if turn == 3:
            print "Game Over"
    # Print (turn + 1) here!
    print "Turn", turn + 1
    print_board(board)
