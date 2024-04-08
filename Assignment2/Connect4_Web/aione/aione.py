# Authors: Catherine Bregou, Willow Gu, Josh Meier
# 4/2/2024

import flask
import json

app = flask.Flask(__name__)

prev_game_id = None
games = {}

def generate_game_id():
    global prev_game_id
    if prev_game_id is None:
         game_id = 1
    else:
        game_id = prev_game_id + 1
    prev_game_id = game_id
    return game_id

@app.route('/newgame/<player>')
def new_game(player):
    
    # generate a new game ID
    gameID = generate_game_id()

    player = player.upper()
    # initialize the game state
    initial_board = '-' * 42
    state = f"{player}#{initial_board}" #player and then initial board.

    games[gameID] = {"state": state, "ai": player}

    return json.dumps({'ID': gameID, 'state': state, 'AI is': player})

'''
when current player is the ai, the program updates the game state (stored in games{}) 
    according to input, have the ai make its move based on this new state, then updates  
    the game state (stored in games{}) to include the ai's move.
when current player is the user, the program updates the game state (stored in games{}) 
    according to input,then returns the input unchanged.
'''
@app.route('/nextmove/<gameID>/<oppCol>/<state>')
def next_move(gameID, oppCol, state):
    
    # update game state
    games[int(gameID)]["state"] = state
    player, board = state.split('#')

    # convert the string to a list of characters
    board_list = list(board)

    # if it is the user's turn, do nothing (keep everything the same)
    if player != games[int(gameID)]["ai"]:
        myCol = oppCol
        new_gamestate = state
        
    if player == games[int(gameID)]["ai"]:
        # update player
        if player == "X":
            next_player = "O"
        if player == "O":
            next_player = "X"

        # ai makes its move
        myCol, new_board_list = makeAIMove(board_list, player)

        # convert the list back to a string
        new_board = ''.join(new_board_list)
        new_gamestate = f"{next_player}#{new_board}"

        games[int(gameID)]["state"] = new_gamestate

    return json.dumps({'ID': gameID, 'col': myCol, 'state': new_gamestate})
                    
def makeAIMove(board_list, player):
    for top_col in range(0, 7):
            if board_list[top_col] == "-":
                for row in range(5, -1, -1):
                    if board_list[row * 7 + top_col] == '-':
                        board_list[row * 7 + top_col] = player
                        myCol = top_col
                        return myCol, board_list



if __name__ == '__main__':
    host = '0.0.0.0'
    port = 1234
    app.run(host=host, port=port, debug=True)