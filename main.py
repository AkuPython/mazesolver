from graphics import Window, Point, Line


def main():
    win = Window(800, 600)
    tl = (2, 2)
    tr = (798, 2)
    bl = (2, 598)
    br = (798, 598)
    top = Line(Point(*tl), Point(*tr))
    bottom = Line(Point(*bl), Point(*br))
    left = Line(Point(*tl), Point(*bl))
    right = Line(Point(*tr), Point(*br))

    win.draw_line(top, "red")
    win.draw_line(bottom, "black")
    win.draw_line(left, "green")
    win.draw_line(right, "blue")
    win.wait_for_close()


if __name__ == "__main__":
    main()

