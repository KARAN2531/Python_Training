import random

# Constants
SIDE = 3

# Function to display the board
def showBoard(board):
    print("\n")
    for i in range(SIDE):
        print(f"\t {board[i][0]} | {board[i][1]} | {board[i][2]}")
        if i < SIDE - 1:
            print("\t-----------")
    print("\n")

# Function to check if any row is completed
def rowCrossed(board):
    return any(board[i][0] == board[i][1] == board[i][2] != ' ' for i in range(SIDE))

# Function to check if any column is completed
def columnCrossed(board):
    return any(board[0][i] == board[1][i] == board[2][i] != ' ' for i in range(SIDE))

# Function to check if any diagonal is completed
def diagonalCrossed(board):
    return (board[0][0] == board[1][1] == board[2][2] != ' ' or
            board[0][2] == board[1][1] == board[2][0] != ' ')

# Function to check if the game is over
def gameOver(board):
    return rowCrossed(board) or columnCrossed(board) or diagonalCrossed(board)

# Function for the user to make a move
def userMove(board):
    while True:
        try:
            r, c = map(int, input("Enter row and column (1-3) to place 'O': ").split())
            if 1 <= r <= 3 and 1 <= c <= 3 and board[r-1][c-1] == ' ':
                board[r-1][c-1] = 'O'
                break
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Enter numbers between 1 and 3.")

# Function for the computer to make a move
def getComputerMove(board):
    empty_cells = [(i, j) for i in range(SIDE) for j in range(SIDE) if board[i][j] == ' ']
    return random.choice(empty_cells)

# Function to play Tic-Tac-Toe
def playTicTacToe():
    board = [[' ' for _ in range(SIDE)] for _ in range(SIDE)]
    showBoard(board)

    # Decide who plays first
    toss = random.randint(0, 1)  # 0 for Computer, 1 for User
    whoseTurn = toss

    moveIndex = 0
    while not gameOver(board) and moveIndex < SIDE * SIDE:
        if whoseTurn == 0:  # Computer move
            r, c = getComputerMove(board)
            board[r][c] = 'X'
            print(f"Computer placed 'X' at row {r+1}, column {c+1}")
        else:  # User move
            userMove(board)

        showBoard(board)
        moveIndex += 1
        whoseTurn = 1 - whoseTurn  # Switch turns

    if not gameOver(board):
        print("It's a draw!")
    else:
        print(f"{'Computer' if whoseTurn == 1 else 'User'} wins!")

# Run the game
playTicTacToe()
