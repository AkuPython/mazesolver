from tkinter import Tk, BOTH, Canvas
import time

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root, bg="black", width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__size = (width, height)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("Window closed...")

    def close(self):
        self.__running = False

    def draw_line(self, line, fill_color="white"):
        line.draw(self.__canvas, fill_color)

    def delete_line(self, line):
        if len(line.tags) == 1:
            self.__canvas.delete(line.tags[0])
        else:
            raise Exception('There needs to be (only) 1 tag')

    def get_size(self):
        return self.__size


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, point_a, point_b):
        self.p1 = point_a
        self.p2 = point_b
        self.__tags = [f"{self.p1.x},{self.p1.y},{self.p2.x},{self.p2.y}"]

    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.p1.x, self.p1.y,
            self.p2.x, self.p2.y,
            fill=fill_color, width=2, tags=self.__tags)

    @property
    def tags(self):
        return self.__tags


class Cell:
    def __init__(self, window, x1, y1, x2, y2, walls=None):
        if walls is None:
            walls = {}
        walls.setdefault('t', True)
        walls.setdefault('b', True)
        walls.setdefault('l', True)
        walls.setdefault('r', True)
        self.walls = walls
        self._p1 = Point(x1, y1)
        self._p2 = Point(x2, y2)
        self._win = window

    def draw(self, fill_color='white'):
        def wall_helper(d, p1, p2):
            '''
            tl = p1x,p1y
            tr = p2x,p1y
            bl = p1x,p2y
            br = p2x,p2y
            top: tl -> tr
            bot: bl -> br
            lef: tl -> bl
            rig: tr -> br
            '''
            match d:
                case 't':
                    line = Line(Point(p1.x, p1.y), Point(p2.x, p1.y))
                case 'b':
                    line = Line(Point(p1.x, p2.y), Point(p2.x, p2.y))
                case 'l':
                    line = Line(Point(p1.x, p1.y), Point(p1.x, p2.y))
                case 'r':
                    line = Line(Point(p2.x, p1.y), Point(p2.x, p2.y))
                case _:
                    raise Exception('invalid wall')
            return line
        for k in self.walls.keys():
            line = wall_helper(k, self._p1, self._p2) 
            if self.walls[k] is True:
                self._win.draw_line(line, fill_color)
            else:
                self._win.delete_line(line)

    def draw_move(self, to_cell, undo=False):
        color = "gray" if undo else "red"
        center1 = Point((self._p1.x + self._p2.x) // 2, (self._p1.y + self._p2.y) // 2)
        center2 = Point((to_cell._p1.x + to_cell._p2.x) // 2, (to_cell._p1.y + to_cell._p2.y) // 2)
        line = Line(center1, center2)
        self._win.draw_line(line, color)


class Maze:
    def __init__(self, window, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y):
        if window is not None and (window.get_size()[0] - x1 < num_cols * cell_size_x or window.get_size()[1] - y1 < num_rows * cell_size_y):
            raise Exception(f'Window size too small...',
                            f'Window={window.get_size()}',
                            f'Row={num_cols} * {cell_size_x} = {num_cols * cell_size_x}',
                            f'Col={num_rows} * {cell_size_y} = {num_rows * cell_size_y}')
        self._win = window
        self._cells = []
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self._create_cells()
        self._break_entrance_and_exit()

    def _create_cells(self):
        x = self.__x1
        for _ in range(self.__num_cols):
            row = []
            y = self.__y1
            for _ in range(self.__num_rows):
                row.append(Cell(self._win, x, y, x + self.__cell_size_x, y + self.__cell_size_y))
                y += self.__cell_size_y
            self._cells.append(row)
            x += self.__cell_size_x
        for i in range(self.__num_cols):
            for j in range(self.__num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        self._cells[i][j].draw()

    def _animate(self):
        self._win.redraw()
        time.sleep(0.1)

    def _break_entrance_and_exit(self):
        self._cells[0][0].walls['t'] = False
        self._draw_cell(0, 0)
        self._cells[-1][-1].walls['b'] = False
        self._draw_cell(-1, -1)



