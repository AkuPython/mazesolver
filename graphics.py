from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root, bg="white", width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False

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
    def __init__(self, window, point_a, point_b, walls=None):
        if walls is None:
            walls = {}
        walls.setdefault('t', True)
        walls.setdefault('b', True)
        walls.setdefault('l', True)
        walls.setdefault('r', True)
        self.walls = walls
        self._p1 = point_a
        self._p2 = point_b
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

