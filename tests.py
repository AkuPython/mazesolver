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
        #self.assertEqual(m1._cells[5][5].walls, {'t': True, 'b': True, 'l': True, 'r': True})
        self.assertEqual(m1._cells[5][5]._p1.__dict__, {'x': 50, 'y': 50})
        self.assertEqual(m1._cells[5][5]._p2.__dict__, {'x': 60, 'y': 60})

    def test_maze_with_seed(self):
        num_cols = 4
        num_rows = 4
        margin = 0
        cell_size_x = 10
        cell_size_y = 10
        maze = Maze(None, margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, 10)
        self.assertEqual(maze._cells.__repr__(), """[[(0.00, 0.00); (10.00, 10.00); ['b', 'l'], (0.00, 10.00); (10.00, 20.00); ['t', 'l', 'r'], (0.00, 20.00); (10.00, 30.00); ['l'], (0.00, 30.00); (10.00, 40.00); ['b', 'l']], [(10.00, 0.00); (20.00, 10.00); ['t', 'r'], (10.00, 10.00); (20.00, 20.00); ['b', 'l'], (10.00, 20.00); (20.00, 30.00); ['t', 'b'], (10.00, 30.00); (20.00, 40.00); ['t', 'b']], [(20.00, 0.00); (30.00, 10.00); ['t', 'b', 'l'], (20.00, 10.00); (30.00, 20.00); ['t', 'r'], (20.00, 20.00); (30.00, 30.00); ['b', 'r'], (20.00, 30.00); (30.00, 40.00); ['t', 'b']], [(30.00, 0.00); (40.00, 10.00); ['t', 'r'], (30.00, 10.00); (40.00, 20.00); ['l', 'r'], (30.00, 20.00); (40.00, 30.00); ['l', 'r'], (30.00, 30.00); (40.00, 40.00); ['r']]]""")

    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(None, 0, 0, num_rows, num_cols, 10, 10)
        for i in m1._cells:
            for j in i:
                self.assertFalse(j.visited)

if __name__ == "__main__":
    unittest.main()

