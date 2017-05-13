"""File to control the game flow."""

import random
import math


class Minesweeper():
    """Minesweeper engine."""

    def __init__(self, input_handler=None, display=None):
        """Set the input handler and ui."""
        self.input_handler = input_handler
        self.display = display

    def generate_board(self, width, height, mineCount=0, mines=None):
        """Generate a new board."""
        # Validate input
        if mineCount >= width * height or mineCount < 0:
            raise ValueError("Invalid number of mines for given board size.")

        if width <= 0 or height <= 0:
            raise ValueError("Width and height of board must " +
                             "both be greater than 0.")

        # generate the board as 2d array of bools
        self.board = ([[False for x in range(0, width)]
                      for y in range(0, height)])

        # distribute mines
        mines = mines or random.sample(range(width * height), mineCount)

        for mine in mines:
            if(mine == 0):
                self.board[0][0] = True
            else:
                self.board[math.floor(mine/width)][mine % width] = True
