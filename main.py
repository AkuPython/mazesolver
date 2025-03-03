from graphics import Window, Point, Line, Cell

def main():
    win = Window(800, 600)
    cell1 = Cell(win, Point(2, 2), Point(12, 12))
    cell1.draw('red')
    cell2 = Cell(win, Point(200, 20), Point(210, 30), walls={'b': False})
    cell2.draw('black')
    cell3 = Cell(win, Point(650, 500), Point(660, 510), walls={'b': False, 'l':False, 't':False})
    cell3.draw('red')
    cell4 = Cell(win, Point(650, 500), Point(660, 510), walls={'r': False})
    cell4.draw('green')
    win.wait_for_close()


if __name__ == "__main__":
    main()

