"""Minesweeper gui."""


import tkinter as tk
from tkinter import messagebox
from minesweeper import Minesweeper, Space


class MinesweeperGUI(tk.Frame, Minesweeper):
    """Minesweeper with gui."""

    default_width = 30
    default_height = 16
    default_dim = 16

    def __init__(self, master=None):
        """Create the game."""
        super().__init__(master)
        self.board_frame = tk.Frame(self).pack(fill=tk.BOTH, expand=tk.YES)
        self.generate_board(width=MinesweeperGUI.default_width,
                            height=MinesweeperGUI.default_height,
                            mine_count=99)
        # self.set_game_board()

    def create_space(self, row, col, is_mine=False):
        """Create a space gui object."""
        s = SpaceGUI(row, col, master=self.board_frame, game=self)
        s.place(width=MinesweeperGUI.default_dim,
                height=MinesweeperGUI.default_dim,
                anchor='nw',
                x=MinesweeperGUI.default_dim*col,
                y=MinesweeperGUI.default_dim*row)
        return s

    def lose(self):
        """End game."""
        messagebox.showerror("DEAD.", "You lose X(")
        self.generate_board(width=MinesweeperGUI.default_width,
                            height=MinesweeperGUI.default_height,
                            mine_count=99)

    def is_won(self):
        """End game if won."""
        if Minesweeper.is_won(self):
            messagebox.showinfo("YES.", "YOU WIN! B)")
            self.generate_board(width=MinesweeperGUI.default_width,
                                height=MinesweeperGUI.default_height,
                                mine_count=99)


class SpaceGUI(tk.Button, Space):
    """Class representing a Space object in the UI."""

    def __init__(self, row, col, game, *args, **kwargs):
        """Create the Space."""
        tk.Button.__init__(self, *args, **kwargs)
        Space.__init__(self)
        self.bind('<Button-1>', self.left_click)
        self.bind('<Button-3>', self.right_click)
        self.bind("<ButtonRelease-1>", self.left_release)
        self.bind("<ButtonRelease-3>", self.right_release)
        self.row = row
        self.col = col
        self.game = game
        self.colors = ['white', 'blue', 'green', 'red', 'purple', 'maroon',
                       'cyan', 'black', 'black']
        self.left_mouse_pressed = False
        self.right_mouse_pressed = False
        self.config(font=("Consolas", 11, "bold"))
        # self.config(command = self.click)

    def left_click(self, event):
        """Try to open the space."""
        self.left_mouse_pressed = True
        if not self.is_open:
            self.game.open_space(self.row, self.col)
        if self.right_mouse_pressed:
            self.chord()
        if self.game.is_won():
            return
        if self.is_mine and self.is_open:
            self.config(bg='red')
            self.game.lose()

    def open(self):
        """Set the text value of the space."""
        Space.open(self)
        self.config(text=Space.__str__(self))
        self.config(fg=self.colors[self.value])
        self.config(bg='ivory2')

    def right_click(self, event):
        """Flag or unflag the space."""
        self.right_mouse_pressed = True
        if self.is_open:
            if self.left_mouse_pressed:
                self.chord()
                self.game.is_won()
            return
        self.is_flagged = not self.is_flagged
        self.config(text=Space.__str__(self))

    def left_release(self, event):
        """Mark left mouse as unpressed."""
        self.left_mouse_pressed = False

    def right_release(self, event):
        """Mark right mouse as unpressed."""
        self.right_mouse_pressed = False

    def chord(self):
        """Chord a space."""
        if not self.is_open:
            return
        to_open = []
        flag_count = 0
        for y in range(-1, 2):
            if y + self.row < 0:
                continue
            if y + self.row >= len(self.game.board):
                break
            for x in range(-1, 2):
                if not (0 <= x + self.col < len(self.game.board[0])) \
                       or x == y == 0:
                    continue
                space = self.game.board[self.row + y][self.col + x]
                flag_count += space.is_flagged
                to_open.append((self.row + y, self.col + x))
        if flag_count == self.value:
            for coord in to_open:
                self.game.open_space(coord[0], coord[1])
                adj = self.game.board[coord[0]][coord[1]]
                if adj.is_mine and adj.is_open:
                    adj.config(bg='red')
                    self.game.lose()
                    return


root = tk.Tk()
app = MinesweeperGUI(master=root)
root.geometry(f'{16*30}x{16*16}')
app.mainloop()
