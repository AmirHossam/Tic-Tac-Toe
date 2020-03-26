#to clear screen
from IPython.display import clear_output
import random

def display_board(board):
    clear_output()
    

    print(' ' + board[7] + ' | ' + board[8] + ' | '+ board[9])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | '+ board[6])
    print('-----------')
    print(' ' + board[1] + ' | ' + board[2] + ' | '+ board[3])



#Function that takes a player input

def player_input():
    marker = ' '
    #Ask the player 1 to choose X or O
    
    while not (marker == 'X' or marker == 'O'):
        marker = input("Player 1 : Do you want X or O ?").upper()
        #if the player 1 chose X so he will pick X and the Player 2 picks O
        if marker == 'X':
            return ('X','O')
        #if the player 1 chose O so he will pick O and the player 2 picks X
        else:
            return ('O','X')

#Function takes in the board list object , a marker ('X' or 'O')
#and desired position (number 1-9)
#and assigns it to the board

def place_marker (board,marker,position):
    board[position]= marker # it will assign the letter X or O to the location


#Function that takes in a board and check if someone won ? 
#it takes 2 arguments "Test_board" and "X or O"
#it prints True if the Chosen Player won

def win_check(board,mark):
    #the possibilites to let some1 win 
    return ((board[7]== mark and board[8]== mark and board[7]== mark)or
    (board[4]== mark and board[5]== mark and board[6]== mark) or
    (board[1]== mark and board[2]== mark and board[3]== mark) or 
    (board[1]== mark and board[5]== mark and board[9]== mark) or
    (board[3]== mark and board[5]== mark and board[7]== mark) or
    (board[2]== mark and board[5]== mark and board[8]== mark) or
    (board[1]== mark and board[4]== mark and board[7]== mark) or
    (board[3]== mark and board[6]== mark and board[9]== mark))


#Function uses random module to decide which player starts first 

def choose_first():
    #random.randint(0,1) => returns a number between 0 and 1 
    if random.randint(0,1)==0:
        return 'Player 2 will start'
    else :
        return 'Player 1 will start'

#Function that returns true or falce if there is a free space 
def space_check(board,position):

    return board[position] == ' '


#Function that check each position in the board is full or not 

def full_board_check(board):
    for i in range(1,10):
        
        if space_check(board,i):
            return False
    return True

#Function asks the player about the next play (1-9)
#uses the "Space Check Function" to check if the next play position 
#is free or not

def player_choice(board):
    position=0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input("Choose your next play : (1-9)"))
        
    return position

#Function asks the players if they want to play again 
#returns boolean expression
#use .startwith('y') to return True if he writes yes
def replay():

    return input('Do you want to play again ?\n Enter Yes or No\n').lower().startswith('y')



#Application :

print("Welcome To XO Game")

while True:
    theBoard = [' ']*10
    player1_marker,player2_marker = player_input()
    turn = choose_first()
    print(turn)
    
    play_game = input("Are you ready to start ?\nEnter Yes or No.\n").lower()

    if play_game[0]=='y':
        game_on = True
    else :
        game_on = False
#>>>Fault is here
    while game_on:

        if turn == 'Player 1':
            #Player's 1 Turn

            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard,player1_marker,position)

            if win_check(theBoard,player1_marker):
                display_board(theBoard)
                print("Congratulations , Player 1 won the game")
                game_on = False
            else : 
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print("The game is a draw")
                    break
                else:
                    turn = 'Player 2'

        else : 
            #Player2's turn

            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard,player2_marker,position)

            if win_check(theBoard,player2_marker):
                display_board(theBoard)
                print("Congratulations , Player 2 won the game")
                game_on = False
            
            else :
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print("the game is a draw!")
                    break
                else:
                    turn = 'Player 1'
    if not replay():
        break