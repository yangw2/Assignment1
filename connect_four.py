'''Conenct 4 code written by Cecilia Ehrlichman, Gisele Nelson, Wesley Yang'''

import flask
import json
import numpy as np

# create a flask variable
app = flask.Flask(__name__)

# store ongoing game IDs
current_id = 0

# take in a 42 character string board_state and output a 6 x 7 2d array representing it
def convert_board(board_state):

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

# return an array (eg [1, 2, 4]) of the possible column indexes where a piece could be played
def get_possible_columns(board):
    cols = []
    for col in range(0, len(board[0])):
        if board[0][col] != "-":
            cols.append(col)
    return cols
        

@app.route('/newgame/<player>')
def new_game(player):
    '''
    Create a new game ID.
    
    '''
    output = {'ID': current_id}
    current_id += 1
    return json.dumps(output) 


@app.route('/nextmove/<gameID>/<oppCol>/<state>')
def next_move(gameID, oppCol, state):
    index = state.find("#")
    player = state[:index]
    board = state[index + 1:]
    board = convert_board(board)
    possible_columns = get_possible_columns(board)
    board = update_state(board, possible_columns)

    output = {'ID': current_id,
              }
    return json.dumps(output) 

def check_gravity(board):
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
    for r in range(0, len(board)):
        for c in range(0, len(board[r])):
            if c + 3 < len(board[r]) and board[r][c] == board[r][c+1] and board[r][c+1] == board[r][c+2] and board[r][c+2] == board[r][c+3]:
                return True
            if r + 3 < len(board) and board[r][c] == board[r+1][c] and board[r+1][c] == board[r+2][c] and board[r+2][c] == board[r+3][c]:
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
        states.append(new_board)
    

if __name__ == "__main__":
    # host = 'localhost'
    # port = 6789
    # app.run(host = host, port = port, debug = True)
    # b1 = "XO-X----XO-X----XO-X----XO-X----XO-X----XO"
    # print(convert_board(b1))
    # print(check_gravity(convert_board(b1)))
    # print(check_fairness(convert_board(b1), "X"))
    # b2 = "-----------------------------------------X"
    # print(len(b2))
    # print(convert_board(b2))
    # print(check_gravity(convert_board(b2)))
    # print(check_fairness(convert_board(b2), "X"))
    # next_move(10, 3, "X#XO-X----XO-X----XO-X----XO-X----XO-X----XO")
