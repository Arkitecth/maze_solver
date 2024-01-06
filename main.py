from graphics import Window

from maze import Maze


def main():
    win = Window(800, 600)
    m1 = Maze(50, 50, 10, 10, 50, 50, win)
    m1._break_entrance_and_exit()
    win.wait_for_close()


main()
