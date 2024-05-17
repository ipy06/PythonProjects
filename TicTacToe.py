import os
import time
from random import randrange

        
def create_empty_board():
    """Create a 3x3 board with 9 empty spaces."""
    
    board = [["j" for i in range(1,4)] for j in range(1,4)] # create the board
    board[1][1] = "X" # and make first move
    return board

def display_board(board):
    """
    The function accepts one parameter containing the board's current status
    and prints it out to the console.
    """

    length_of_row = len(board)

    # Iterating through the 3x3 board and assigning indexes
    for i in range (1, (length_of_row ** 2 + 1)):
        if board[(i - 1) // length_of_row][(i - 1) % length_of_row] not in ("X","O"):
                board[(i - 1) // length_of_row][(i - 1) % length_of_row] = i

    
    # printing out the board
    print("+-------+-------+-------+\n|       |       |       |")
    print("|  ",board[0][0],"  |  ",board[0][1],"  |  ",board[0][2],"  |")
    print("|       |       |       |")
    print("+-------+-------+-------+\n|       |       |       |")
    print("|  ",board[1][0],"  |  ",board[1][1],"  |  ",board[1][2],"  |")
    print("|       |       |       |")
    print("+-------+-------+-------+\n|       |       |       |")
    print("|  ",board[2][0],"  |  ",board[2][1],"  |  ",board[2][2],"  |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
   

def get_user_move(board):
    """
    The function accepts the board's current status, asks the user about their move, 
    checks the input, and updates the board according to the user's decision.
    """


    while True:
        try:
            move = int(input("\nEnter your move: "))             # Get user input           
        except ValueError:
            print("Invalid input. Please enter an integer number.")
            continue
        
        if type(move) == int:
            if move > 0 and move < 10:                      
                if board[(move-1)//3][(move-1)%3] not in ("X", "O"):   # check if available spot
                    board[(move-1)//3][(move-1)%3] = "O"
                    break
                else:
                    print("This cell is already occupied. Choose another one!")
            else:
                print("Invalid input. Please enter a number between 1 and 9.")
        else:
            print("Invalid input. Please enter a number between 1 and 9.")
            
    return display_board(board)



def make_list_of_free_fields(board):
    """
    The function browses the board and builds a list of all the free squares; 
    the list consists of tuples, while each tuple is a pair of row and column numbers.
    """

    free_fields = []            # Empty List

    for i in range (len(board)):
        for j in range (len(board[0])):
            if board[i][j] not in ("X", "O"):
                free_fields.append((i,j))     # add tuples of unoccupied indexes to free fields

    
    return free_fields


def victory_for(board, sign):
    """
    The function analyzes the board's status in order to check if 
    the player using 'O's or 'X's has won the game

    The function checks the horizontal, vertical, and diagonal lines.
    It returns 'True' if all cells along a line have been filled by the player's sign,
    returns 'False' in other case.
    """

    # List of Horizontal, Vertical and Diagonal lines
    list_of_lines = [ board[0], board[1], board[2], 
                     [board[0][0], board[1][1], board[2][2]], 
                     [board[0][2], board[1][1], board[2][0]], 
                     [board[0][0], board[1][0], board[2][0]], 
                     [board[0][1], board[1][1], board[2][1]], 
                     [board[0][2], board[1][2], board[2][2]]
                    ]


    if sign == "X":
        
        for lines in list_of_lines:
            if lines.count("X") ==  3:  # X's win condition
                return True
        
    elif sign == "O":

        for lines in list_of_lines:
            if lines.count("O") ==  3:  # O's win condition
                return True
    
    else:

        print("Invalid Sign")   # bad call

    return False


def draw_move(board):
    """The function draws the computer's move and updates the board."""


    # List of Horizontal, Vertical and Diagonal lines
    list_of_lines = [ board[0], board[1], board[2], 
                     [board[0][0], board[1][1], board[2][2]], 
                     [board[0][2], board[1][1], board[2][0]], 
                     [board[0][0], board[1][0], board[2][0]], 
                     [board[0][1], board[1][1], board[2][1]], 
                     [board[0][2], board[1][2], board[2][2]]
                    ]
    

    # Traversing the List of lines
    for line in list_of_lines:
        if ((line.count("X") == 2) and (line.count("O") == 0)):  # check for a winning move
            for elem in line:
                if elem != "X":
                    board[(elem - 1) // 3][(elem - 1) % 3] = "X" # winning move
                    print("\nI have made my move.")
                    return display_board(board)

        # Uncomment condition below to make it Impossible to beat or alternate with above
          
        # if ((line.count("O") == 2) and (line.count("X") == 0)): # check for a block move
        #     for elem in line:
        #         if elem != "O":
        #             board[(elem - 1) // 3][(elem - 1) % 3] = "X"  # block move
        #             print("\nI have made my move.")
        #             return display_board(board)
        
    

    made_move = False
    free_fields = make_list_of_free_fields(board) 


    # make a random move in the available spots
    while not made_move:
        
        move = randrange(1, 10)
        if ((move - 1) // 3 , (move - 1) % 3 ) in free_fields:
            board[(move - 1) // 3][(move - 1) % 3] = "X"
            made_move = True
        else:
            made_move = False
    
    time.sleep(2)  
    print("\nI have made my move.")
    return display_board(board)
    

def remove_string_duplicates(string):
    """
    This function removes the duplicates in a string and 
    returns a new duplicate-free string
    """

    duplicate_free = ""
    for char in string:
        if char not in duplicate_free:
            duplicate_free = duplicate_free+char
    return duplicate_free


def play_again():
    """
    This function asks a user if they want to play again then starts the game again
    if the answer is "yes" and ends the program if their answer is "no"
    """
    play_again_input = False
    while not(play_again_input):
        try:
            play_again = input("\nWould you like to play again (yes/no) ? ").lower()
        except ValueError:
            print("Invalid input, please try again.")
            continue
        except TypeError:
            print("Invalid input, please try again.")
        
        play_again_input = True
        play_again = remove_string_duplicates(play_again)    # in case of mistyped answers (e.g. yyess)
        if play_again == "yes":
            return start()
        elif play_again == "no":
            return bye()
        else:
            print("You did not give a valid answer so you will be asked again\n")
            play_again_input = False


def bye():
    """
    This function ends the program
    """

    print("\nThank you for playing Tic Tac Toe!")
    print("""
=========
+ Byee! +
=========
          """)
    time.sleep(1)                 # wait 1 second
        

def main(board):
    """
    The main function of the game. It displays the board and asks the user for a move.
    The function updates the board, and checks whether the game has ended.
    If the game has not ended, the function calls itself again.
    The computer has the first move and it plays with X's
    """

    decision = False                    # A conclusion is yet to be drawn

    if (len(make_list_of_free_fields(board)) > 0):          # check for draw
        get_user_move(board)                             # call for player move
        if (victory_for(board, "O")):                 # check for player win
            print("\nYou Won!\n")
            time.sleep(1)                             
            decision = True             # A conclusion has been drawn
            return play_again()                       
        draw_move(board)                              # computer move
        if (victory_for(board, "X")):                 # check for computer win
            print("\nYou Lost, I won!\n")
            time.sleep(1)                             
            decision = True             # A conclusion has been drawn
            return play_again()
    else:
        print("\nDraw!\n")
        time.sleep(1)
        decision = True                 # A conclusion has been drawn
        return play_again()

    if not decision:
        main(board)                 # recursively call to continue the game


def start():

    if ((os.name).lower() == "windows"):      # depending on the Operating System
        os.system("cls")                      # use "cls" or "clear" to clear the screen
    else:
        os.system("clear")

    print("""
======================================
+                                    +
+ Welcome to my game of Tic Tac Toe! +
+                                    +
======================================         
            """)
    board = create_empty_board()                        
    print("\nI have made the first move.\n")
    display_board(board)
    main(board)
        
            
try:
    start()
except KeyboardInterrupt:                   # Termination of program with a keyboard command such as "Ctrl+C"
    print("\n\nThanks for playing!")
    time.sleep(1)
except:
    print("\n\nAn unforseen error occured!")
    