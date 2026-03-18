# Critical Mass 💣

**Critical Mass** is a bot-making competition based on the explosive strategic game **Chain Reaction**! This repository serves as your official battleground and toolkit to build, test, and submit your AI champion.

This repository contains game logic, simulation scripts, and tournament management code.

## 🎮 Game Overview
Chain Reaction is a strategic 2-player board game played on a 12×8 grid.
1. Players take turns placing 1 orb into either an **empty cell** or a cell **they already own**.
2. Every cell has a **critical mass** (capacity) depending on its location:
   * **Corners:** 2 orbs
   * **Edges:** 3 orbs
   * **Middles:** 4 orbs
3. When a cell reaches its critical mass, it **explodes!** It shoots 1 orb into each of its directly adjacent (up, down, left, right) neighbors.
4. If the exploding orbs land in a cell owned by the opponent, the exploding player **takes ownership** of that cell and all the orbs inside it!
5. Explosions can push neighboring cells past their capacity, triggering a massive **chain reaction**.
6. **Winner:** Once both players have placed their first orb, a player instantly wins if they wipe the opponent off the board (the opponent has 0 owned cells left).

## Goal of the Competition
Create the best bot that can beat other bots in Critical Mass (Chain Reaction).

## Repo Structure
* **`chain_reaction.py`**: The core game engine. Handles the physics, explosions, orb conservation, and victory detection.
* **`play_match.py`**: The match runner. You use this script to duel two bots against each other. It includes crash protection to prevent poor bot code from crashing the match.
* **`dummy_bot.py`**: An incredibly simple template bot. It just finds the very first valid cell and plays there.
* **`random_bot.py`**: A slightly smarter template bot that picks a completely random valid move inside the grid.

## How Bots Work
Each bot is a Python file and must implement the following function:

```python
def get_move(state, player_id):
    # state: 12x8 current board state matrix. Each item is a tuple: (owner_id, orb_count). 
    #        If the cell is empty, it will be (None, 0).
    # player_id: Your assigned player ID (0 or 1).
    # Return: (row, col) of your move. You can only place on your own tiles or empty tiles!
    ...
```

Check out `dummy_bot.py` or `random_bot.py` for a practical example.

## How to Submit Your Bot
To participate in the tournament, submit your bot as a single Python file containing your `get_move` function (e.g., `yourname_bot.py`). Make sure your bot logic is entirely contained within this file. Ensure your bot executes efficiently to avoid being forfeited for exceeding tournament move time limits.
x  xx