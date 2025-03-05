from graphics import Window, Point, Line, Cell, Maze

def main():
    num_cols = 16
    num_rows = 12
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    win = Window(screen_x, screen_y)
    maze = Maze(win, margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, 10)
    maze.solve()
    win.wait_for_close()


if __name__ == "__main__":
    main()

