from graphics import Window

from maze import Maze


def main():
    win = Window(800, 600)
    m1 = Maze(50, 50, 10, 10, 50, 50, win, seed=5)
    print(m1.solve())
    win.wait_for_close()


main()
