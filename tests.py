import unittest

from graphics import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(None, 0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
        self.assertEqual(m1._cells[5][5].walls, {'t': True, 'b': True, 'l': True, 'r': True})
        self.assertEqual(m1._cells[5][5]._p1.__dict__, {'x': 550, 'y': 60})
        self.assertEqual(m1._cells[5][5]._p2.__dict__, {'x': 560, 'y': 70})

if __name__ == "__main__":
    unittest.main()

