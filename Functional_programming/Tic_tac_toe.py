
#========Global Variables=========

#=====Game Board====

board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

#If game is still going

game_still_going = True

#Who won? or Tie?
winner = None

#Who's turn is it
current_player = "X"

#list to keep track of the inputs
lissi = []


#Display the board in between
def display_board():
    print(board[0]," | ",board[1]," | ",board[2])
    print(board[3]," | ",board[4]," | ",board[5])
    print(board[6]," | ",board[7]," | ",board[8])


#Play a game of Tic-Tac-Toe
def play_game():
    
    select_symbol()
    #Display initial board
    display_board()
    
    #While the game is still going
    while game_still_going:
        #Handle a single turn of any player
        handle_turn(current_player)
        #Check if the game has ended
        check_if_game_over()
        #Flip to the other player
        flip_plyrs()
    #The game has ended
    if winner == "X" or winner =="O":
        print("\t\t\t\t" + '\033[1m \033[91m \033[4m' + winner + " WON!!")
    elif winner == None:
        print("\t\t\t\t" + "The game is a tie!!")
  

#Function to choose the symbol needed for game 
def select_symbol():
    global current_player
    current_player = input("Which symbol do you want? (Choose: X|O): ")
    if(current_player == "O" or current_player == "X"):
        pass
    else:
        select_symbol()
    return


def handle_turn(player):

    print(current_player +"'s Turn")
    position = input("Enter the position from 1-9: ")
    
    valid = True
    
    while valid:
        
        while position not in ["1", "2", "3", "4","5","6", "7", "8", "9"]:
            position = input("Choose a number from 1-9: ")
            
        position = int(position) - 1 
        
        if board[position] == "-":
            valid = False
        else:
            print("Enter another position!!!!")    

    #Changing postion to match the index
    board[position] = (current_player)
    
    display_board()
    return


def check_if_game_over():
    check_if_win()
    check_if_tie()


def check_if_win():
    
    global winner
    #check rows
    row_winner = check_rows() 
    #check columns
    column_winner = check_columns()
    #check diagonals
    diagonal_winner = check_diagonals()
    
    if row_winner:
        winner = row_winner
        return
    elif column_winner:
        winner = column_winner
        return
    elif diagonal_winner:
        winner = diagonal_winner
        return
    else:
        #The game is tie
        return
    return



def check_rows():
    
    global game_still_going 
    #Check if the rows are having same values
    row_1 = board[0] == board[1] == board[2] !="-"
    row_2 = board[3] == board[4] == board[5] !="-"
    row_3 = board[6] == board[7] == board[8] !="-"
    
    #if any of the row have the same value then game_still_going is false so as to end the game
    if row_1 or row_2 or row_3:
        game_still_going = False
        
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6] 
    return



def check_columns():
    
    global game_still_going 
    #Check if the columns are having same values
    column_1 = board[0] == board[3] == board[6] !="-"
    column_2 = board[1] == board[4] == board[7] !="-"
    column_3 = board[2] == board[5] == board[8] !="-"
    
    #if any of the column have the same value then game_still_going is false so as to end the game
    if column_1 or column_2 or column_3:
        game_still_going = False
        
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]        
    return


def check_diagonals():
    
    #Check if any of the diagonals are having same values
    global game_still_going
    
    diagonal_1 = board[0] == board[4] == board[8] !="-"
    diagonal_2 = board[2] == board[4] == board[6] !="-"
    
    #if any of the diagonals have the same value then game_still_going is false so as to end the game
    if diagonal_1 or diagonal_2:
        game_still_going = False
    
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    return



def check_if_tie():
    
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return


def flip_plyrs():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return
    
play_game()