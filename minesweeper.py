"""File to control the game flow."""

import random
import math


class Space():
    """Class representing a space on the board."""

    def __init__(self, is_mine=False, row=None, col=None):
        """Set bools on the space."""
        self.is_mine = is_mine
        self.is_open = False
        self.is_flagged = False
        self.value = 0
        self.row = row
        self.col = col

    def __str__(self):
        """Return value if open, else blank space or F."""
        if self.is_flagged:
            return "F"
        if not self.is_open:
            return " "
        if self.is_mine:
            return "X"
        return str(self.value)

    def __repr__(self):
        """Return value if open, else blank space or F."""
        return self.__str__()


class Minesweeper():
    """Minesweeper engine."""

    def generate_board(self, width, height, mine_count=0, mines=None):
        """Generate a new board."""
        # Validate input
        if mine_count >= width * height or mine_count < 0:
            raise ValueError("Invalid number of mines for given board size.")

        if width <= 0 or height <= 0:
            raise ValueError("Width and height of board must " +
                             "both be greater than 0.")
        self.width = width
        self.height = height
        self.hit_mine = False
        self.open_count = 0
        self.board = ([[Space(is_mine=False, row=y, col=x)
                      for x in range(0, width)]
                      for y in range(0, height)])

        # distribute mines
        mines = mines or random.sample(range(width * height), mine_count)
        self.mine_count = len(mines)
        self.target_count = width * height - self.mine_count
        for mine in mines:
            if(mine == 0):
                self.board[0][0].is_mine = True
            else:
                self.board[math.floor(mine/width)][mine % width].is_mine = True

    def open_space(self, row, col):
        """Open a space on the board.

        If no surrounding mines, will recursively call on adj spaces.
        """
        if not (0 <= row < len(self.board) and 0 <= col < len(self.board[0])):
            return
        space = self.board[row][col]
        if space.is_flagged or space.is_open:
            return

        space.is_open = True
        to_open = []
        if space.is_mine:
            self.hit_mine = True
            space.value = -1
        else:
            space.value = 0
            # count surrounding mines
            for y in range(-1, 2):
                if y + row < 0:
                    continue
                if y + row >= len(self.board):
                    break
                for x in range(-1, 2):
                    if not (0 <= x + col < len(self.board[0])) or x == y == 0:
                        continue
                    space.value += self.board[row + y][col + x].is_mine
                    to_open.append((row + y, col + x))
        if space.value == 0:
            while len(to_open) > 0:
                coord = to_open.pop(0)
                self.open_space(coord[0], coord[1])
