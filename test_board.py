"""Minesweeper unit tests."""


import minesweeper
import unittest


class TestMinesweeper(unittest.TestCase):
    """Tests for the game."""

    def test_generate_board_no_mines(self):
        """Test the board generates successfully with no mines."""
        # arrange
        game = minesweeper.Minesweeper()
        width = 10
        height = 12

        # act
        game.generate_board(width, height, 0)

        # assert
        self.assertEqual(width, len(game.board[0]), 'Board width incorrect.')
        self.assertEqual(height, len(game.board), 'Board height incorrect.')

        for row in range(height):
            self.assertFalse(any(game.board[row]),
                             ("Mine found when board was generated " +
                              "with mineCount = 0."))

    def test_generate_board_max_mines(self):
        """Test the board generator with the max number of mines."""
        # arrange
        game = minesweeper.Minesweeper()
        width = 10
        height = 12

        # act
        game.generate_board(width, height, width * height - 1)

        # assert
        self.assertEqual(width, len(game.board[0]), 'Board width incorrect.')
        self.assertEqual(height, len(game.board), 'Board height incorrect.')

        minesFound = (sum(game.board[row][col] for col in range(width)
                      for row in range(height)))

        self.assertEqual(width * height - 1, minesFound,
                         'Wrong number of mines found.')

    def test_generate_board_width_greater_than_height(self):
        """Test the board generator succeeds with width > height."""
        # arrange
        game = minesweeper.Minesweeper()
        width = 19
        height = 10
        mines = int(width * height / 2)

        # act
        game.generate_board(width, height, mines)

        # assert
        self.assertEqual(width, len(game.board[0]), 'Board width incorrect.')
        self.assertEqual(height, len(game.board), 'Board height incorrect.')

        minesFound = (sum(game.board[row][col] for col in range(width)
                      for row in range(height)))

        self.assertEqual(mines, minesFound,
                         'Wrong number of mines found.')

    def test_generate_board_height_greater_than_width(self):
        """Test the board generator with height > width."""
        # arrange
        game = minesweeper.Minesweeper()
        width = 9
        height = 17
        mines = int(width * height / 2)

        # act
        game.generate_board(width, height, mines)

        # assert
        self.assertEqual(width, len(game.board[0]), 'Board width incorrect.')
        self.assertEqual(height, len(game.board), 'Board height incorrect.')

        minesFound = (sum(game.board[row][col] for col in range(width)
                      for row in range(height)))

        self.assertEqual(mines, minesFound,
                         'Wrong number of mines found.')

    def test_generate_board_height_equal_to_width(self):
        """Test the board generator at height == width."""
        # arrange
        game = minesweeper.Minesweeper()
        width = 20
        height = 20
        mines = int(width * height / 2)

        # act
        game.generate_board(width, height, mines)

        # assert
        self.assertEqual(width, len(game.board[0]), 'Board width incorrect.')
        self.assertEqual(height, len(game.board), 'Board height incorrect.')

        minesFound = (sum(game.board[row][col] for col in range(width)
                      for row in range(height)))
        self.assertEqual(mines, minesFound,
                         'Wrong number of mines found.')

    def test_generate_board_too_many_mines_errors(self):
        """Test the board generator fails when too many mines supplied."""
        # arrange
        game = minesweeper.Minesweeper()
        width = 10
        height = 12
        mines = int(width * height)

        # act and expect error
        with self.assertRaises(ValueError):
            game.generate_board(width, height, mines)

    def test_generate_board_negative_mines_errors(self):
        """Test the board generator fails when <0 mines supplied."""
        # arrange
        game = minesweeper.Minesweeper()
        width = 10
        height = 12
        mines = -1

        # act and expect error
        with self.assertRaises(ValueError):
            game.generate_board(width, height, mines)


if __name__ == '__main__':
    unittest.main()
