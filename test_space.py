"""Tests for the Space class."""

import unittest
from minesweeper import Space, Minesweeper


class TestSpace(unittest.TestCase):
    """Test cases for the Space class."""

    def test_open_opens_all_adjacent_when_mine_count_0_with_corners(self):
        """Opening a 0 space should open all adjacent spaces."""
        # arrange
        ms = Minesweeper()
        ms.board = [
                 [Space(False), Space(False), Space(False)],
                 [Space(False), Space(False), Space(False)],
                 [Space(False), Space(False), Space(False)]
                ]
        # act
        ms.open_space(1, 1)
        print(ms.board)
        # assert
        self.assertTrue(all([col.is_open for row in ms.board for col in row]),
                        'Not all spaces open.')

    def test_open_space_with_adjacent_mine_sets_value_does_not_open_adj(self):
        """Open a space that has mines adjacent."""
        # arrange
        ms = Minesweeper()
        ms.board = [
                 [Space(True), Space(False), Space(False)],
                 [Space(False), Space(False), Space(False)],
                 [Space(False), Space(True), Space(False)]
                ]
        # act
        ms.open_space(1, 1)
        # assert
        self.assertTrue(ms.board[1][1].is_open, 'Space not opened')
        self.assertFalse(any([ms.board[row][col].is_open
                             for row in range(3)
                             for col in range(3)
                             if not (row == 1 and col == 1)]),
                         'Adjacent space opened.')

    def test_open_flagged_space_should_do_nothing(self):
        """Open a space that has been flagged."""
        # arrange
        ms = Minesweeper()
        ms.board = [
                 [Space(False), Space(False), Space(False)],
                 [Space(False), Space(False), Space(False)],
                 [Space(False), Space(False), Space(False)]
                ]
        ms.board[1][1].is_flagged = True
        # act
        ms.open_space(1, 1)
        # assert
        self.assertFalse(ms.board[1][1].is_open, 'Flagged space opened.')
        self.assertTrue(all([not col.is_open for row in ms.board
                             for col in row]),
                        'Flagged space should not have opened adj.')

    def test_open_mine_opens_just_that_space(self):
        """Open a space that's a mine."""
        # arrange
        ms = Minesweeper()
        ms.board = [
                 [Space(False), Space(False), Space(False)],
                 [Space(False), Space(True), Space(False)],
                 [Space(False), Space(False), Space(False)]
                ]
        # act
        ms.open_space(1, 1)
        # assert
        self.assertTrue(ms.board[1][1].is_open, 'Space not opened.')
        self.assertFalse(any([ms.board[row][col].is_open
                             for row in range(3)
                             for col in range(3)
                             if not (row == 1 and col == 1)]),
                         'Adjacent spaces opened.')


if __name__ == '__main__':
    unittest.main()
