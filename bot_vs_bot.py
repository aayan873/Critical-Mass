from chain_reaction import ChainReactionGame

# Pick which bots to run by changing these imports
import dummy_bot as bot0
import random_bot as bot1

def print_board(state):
    for row in state:
        parts = []
        for owner, count in row:
            if owner is None or count == 0:
                parts.append("__")
            else:
                parts.append(f"{owner}{count}")
        print(" ".join(parts))


def main():
    rows, cols = 12, 8 
    max_turns = 1000

    game = ChainReactionGame(rows=rows, cols=cols)
    bots = {0: bot0.get_move, 1: bot1.get_move}

    for turn in range(max_turns):
        player = turn % 2
        
        try:
            move = bots[player](game.get_state(), player)
            print(f"Turn {turn + 1}: Player {player} plays {move}")
            
            game.apply_move(player, move)
            print_board(game.get_state())
            
        except Exception as e:
            winner = 1 - player
            print(f"Player {player} forfeits (crashed or made invalid move): {e}")
            print(f"Winner: Player {winner}")
            return

        winner = game.check_winner()
        if winner is not None:
            print("Final board:")
            print_board(game.get_state())
            print(f"Winner: Player {winner}")
            return

    print("Reached max_turns without a winner.")
    print("Final board:")
    print_board(game.get_state())

if __name__ == "__main__":
    main()
