#! /usr/bin/env python3

import re
import pytest

def check_pattern(board_state):
    winning_patterns = ["XXX.", ".XXX", "X..X..X..", ".X..X..X.",
                        "..X..X..X", "X...X...X", "..X.X.X..",
                        "OOO.", ".OOO", "O..O..O..", ".O..O..O.",
                        "..O..O..O", "O...O...O", "..O.O.O.."]
    is_there_a_match = False

    for pattern in winning_patterns:
        if re.search(pattern, board_state):
            is_there_a_match = True
            break

    return is_there_a_match

def is_move_valid(board="", move=""):
    return (len(move) == 2 and int(move[0]) in range(1, 10)
            and move[1].capitalize() in ('X', 'O'))

def main():
    board_display = """
    -------
|1|2|3|
-------
|4|5|6|
-------
|7|8|9|
------- """.strip()

    board_mapping = "123456789"

    while True:
        print(board_display)
        move = input("What's your move? (q to quit): ")
        if move[0].capitalize() == "Q":
            break
        else:
            if is_move_valid(board_mapping, move):
                board_mapping = board_mapping.replace(move[0], move[1].capitalize())
                board_display = board_display.replace(move[0], move[1].capitalize())
                if check_pattern(board_mapping):
                    print(board_display)
                    print("We have a winner!!!")
                    break
            else:
                print("Invalid move! Try again.")

if __name__ == "__main__":
    main()