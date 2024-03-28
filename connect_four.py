'''Connect 4 code written by Cecilia Ehrlichman, Gisele Nelson, Wesley Yang'''

import flask
import json
import numpy as np
import random

# create a flask variable
app = flask.Flask(__name__)

# store ongoing game IDs
current_id = 0

def board_string_to_array(board_state):
    '''
        Takes a 42 character string representation of the board and returns a corresponding 6 x 7 2d array
    '''
    if len(board_state) != 42:
        print("Error: invalid board size")
        return
        
    new_board = []
    for r in range(0, 6):
        new_board.append([])
        for c in range(0, 7):
            new_board[r].append(board_state[0])
            board_state = board_state[1:]
    return np.array(new_board)

def board_array_to_string(board_state):
    '''
        Takes a 2d representation of the board and returns it in string format
    '''
    new_board = ""
    for r in range(0, 6):
        for c in range(0, 7):
            new_board += board_state[r][c]
    return new_board

# return an array (eg [1, 2, 4]) of the possible column indexes where a piece could be played
def get_possible_columns(board):
    '''
        Identifies the columns in the board that are available
    '''
    cols = []
    for col in range(0, len(board[0])):
        if board[0][col] == "-":
            cols.append(col)
    return cols
        

@app.route('/newgame/<player>')
def new_game(player):
    '''
    Create a new game ID.
    
    '''
    global current_id
    output = {'ID': current_id}
    current_id += 1
    return json.dumps(output) 


@app.route('/nextmove/<gameID>/<oppCol>/<state>')
def next_move(gameID, oppCol, state):
    '''
        Takes a gameID, the column the opponent just dropped a piece in, and state (the current board configuration)
        Gets possible columns the AI could play in and updates board
        Returns JSON object with game ID, column played in, and the new board configuration in string form
    '''
    index = state.find("#")
    player = state[:index]
    board = state[index + 1:]
    board = board_string_to_array(board)
    possible_columns = get_possible_columns(board)
    
    print(board)
    # if there is no possible move for the AI, set column to -1 and return the original board
    if len(possible_columns) == 0:
        column = -1
    else:
        board, column = update_state(board, possible_columns, player)
    
    board_str = board_array_to_string(board)
    print(board)
    output = {'ID': gameID,
              'col': column,
              'state': board_str}
    return json.dumps(output) 

def check_gravity(board):
    '''
        Repeatedly checks if the players piece has another piece below it, if it doesn't then 
        the piece will move down one row
    '''
    for column in board.T:
        i = 0
        while i < 6 and column[i] == '-':
            i += 1
        while i < 6 and not column[i] == '-':
            i +=1
        if i < 6:
            return False
    return True

def check_fairness(board, player):
    '''
        Records the amount of moves that the players have made, if the difference in number of 
        moves between the two players is greater than 1 then return False
    '''
    x = 0
    o = 0
    for row in board:
        for entry in row:
            if entry == 'X':
                x += 1
            if entry == 'O':
                x += 1
    if player == "X":
        if o - 1 == x or o == x:
            return True
    if player == "O":
        if x - 1 == o or o == o:
            return True
    return False 
            

def check_win(board):
    '''
        Returns True or False representing whether a player has won in the given board configuration
        Checks for wins horizontally, vertically, and diagonally
    '''
    for r in range(0, len(board)):
        for c in range(0, len(board[r])):
            if board[r][c] == "X" or board[r][c] == "O":
                if c + 3 < len(board[r]) and board[r][c] == board[r][c+1] and board[r][c+1] == board[r][c+2] and board[r][c+2] == board[r][c+3]:
                    return True
                if r + 3 < len(board) and board[r][c] == board[r+1][c] and board[r+1][c] == board[r+2][c] and board[r+2][c] == board[r+3][c]:
                    return True
    # check for right slanting diagonal wins
    for start_i in range(3):
        for start_j in range(4):
            if not board[start_i][start_j] == '-':
                win = True
                for i in range(1, 4):
                    if not board[start_i][start_j] == board[start_i + i][start_j + i]:
                        win = False
                if win == True:
                    return True
    # check for left slanting diagonal wins
    for start_i in range(3):
        for start_j in range(3, 7):
            if not board[start_i][start_j] == '-':
                win = True
                for i in range(1, 4):
                    if not board[start_i][start_j] == board[start_i + i][start_j - i]:
                        win = False
                if win == True:
                    return True

        
    return False

def update_state(board, possible_columns, player):
    '''
    If a winning move exists choose that move, otherwise select a random move.
    '''
    states = []
    for column in possible_columns:
        i = 0
        while i < 6 and board[i][column] == "-":
            i += 1
        i -= 1
        new_board = np.copy(board)
        new_board[i][column] = player
        states.append((new_board, column))
        if check_win(new_board):
            return new_board, column
    return random.choice(states)
    

if __name__ == "__main__":
    host = 'localhost'
    port = 6789
    app.run(host = host, port = port, debug = True)
    