"""Minesweeper gui."""


import tkinter as tk
from minesweeper import Minesweeper, Space


class MinesweeperGUI(tk.Frame):

    default_width = 30
    default_height = 16
    default_dim = 16

    def __init__(self, master=None):
        super().__init__(master)
#        self.create_widgets()
        self.game = Minesweeper()
        self.game.generate_board(width=MinesweeperGUI.default_width,
                                 height=MinesweeperGUI.default_height,
                                 mine_count=99)
        self.board = tk.Frame(self).pack(fill=tk.BOTH, expand=tk.YES)
        self.set_game_board()

    def set_game_board(self):
        for row in range(len(self.game.board)):
            for col in range(0, len(self.game.board[0])):
                b = SpaceGUI(master=self.board,
                             text=self.game.board[row][col],
                             space=self.game.board[row][col],
                             game=self.game)
                b.place(width=MinesweeperGUI.default_dim,
                        height=MinesweeperGUI.default_dim,
                        anchor='nw',
                        x=MinesweeperGUI.default_dim*col,
                        y=MinesweeperGUI.default_dim*row)

    def click_space(self, spaceGUI, row, col):
        self.game.open_space(row, col)
        spaceGUI.click()


class SpaceGUI(tk.Button):
    def __init__(self, space, game, *args, **kwargs):
        tk.Button.__init__(self, *args, **kwargs)
        self.space = space
        self.game = game
        self.config(command = self.click)

    def click(self):
        self.game.open_space(self.space.row, self.space.col)
        self.config(text=self.space)




root = tk.Tk()
app = MinesweeperGUI(master=root)
root.geometry(f'{16*30}x{16*16}')
app.mainloop()
