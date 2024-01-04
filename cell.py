from graphics import Line, Point


class Cell:
    def __init__(self, win=None) -> None:
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = 0
        self._x2 = 0
        self._y1 = 0
        self._y2 = 0
        self._win = win

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

        if self.has_left_wall:
            line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            self._win.draw_line(line)
        if self.has_right_wall:
            line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            self._win.draw_line(line)
        if self.has_top_wall:
            line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            self._win.draw_line(line)
        if self.has_bottom_wall:
            line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            self._win.draw_line(line)

    def draw_move(self, to_cell, undo=False):
        fill = "gray"
        if undo == False:
            fill = "red"

        current_cell_midpoint_x = (self._x1 + self._x2) / 2
        current_cell_midpoint_y = (self._y1 + self._y2) / 2
        to_cell_midpoint_x = (to_cell._x1 + to_cell._x2) / 2
        to_cell_midpoint_y = (to_cell._y1 + to_cell._y2) / 2

        line = Line(Point(current_cell_midpoint_x, current_cell_midpoint_y), Point(
            to_cell_midpoint_x, to_cell_midpoint_y))
        self._win.draw_line(line, fill)
