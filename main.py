from graphics import Window, Point, Line, Cell, Maze
import sys
sys.setrecursionlimit(10000)

def main():
    num_cols = 96
    num_rows = 72
    margin = 20
    screen_x = 1200
    screen_y = 900
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    win = Window(screen_x, screen_y)
    maze = Maze(win, margin, margin, num_rows, num_cols, cell_size_x, cell_size_y) #, 10)
    if maze.solve():
        print('SOLVED')
    else:
        print('Bad maze! Cannot be solved')
    win.wait_for_close()


if __name__ == "__main__":
    main()

