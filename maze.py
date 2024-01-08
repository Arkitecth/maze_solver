from cell import Cell
import time
import random


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None) -> None:
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = []
        if seed != None:
            random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):
        for i in range(self.num_rows):
            self._cells.append([])
            for j in range(self.num_cols):
                self._cells[i].append(Cell(self.win))

        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self.win == None:
            return
        x1 = self.x1 + (j * self.cell_size_x)
        x2 = x1 + self.cell_size_x
        y1 = self.y1 + (i * self.cell_size_y)
        y2 = y1 + self.cell_size_y

        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self.num_rows-1][self.num_cols-1].has_bottom_wall = False
        self._draw_cell(self.num_rows-1, self.num_cols-1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True

        while True:
            to_be_visited = []
            # Check the cells that are directly adjacent to the current cell
            # Right
            if j + 1 < self.num_cols and self._cells[i][j+1].visited == False:
                to_be_visited.append(("Right", i, j+1))
            # Left
            if j - 1 >= 0 and self._cells[i][j-1].visited == False:
                to_be_visited.append(("Left", i, j-1))
            # Up
            if i - 1 >= 0 and self._cells[i-1][j].visited == False:
                to_be_visited.append(("Up", i-1, j))
            # Down
            if i + 1 < self.num_rows and self._cells[i+1][j].visited == False:
                to_be_visited.append(("Down", i+1, j))

            if len(to_be_visited) == 0:
                self._draw_cell(i, j)
                return
            else:
                random_direction = random.choice(to_be_visited)
                if random_direction[0] == "Right":
                    self._cells[i][j].has_right_wall = False
                    self._cells[random_direction[1]
                                ][random_direction[2]].has_left_wall = False
                elif random_direction[0] == "Left":
                    self._cells[i][j].has_left_wall = False
                    self._cells[random_direction[1]
                                ][random_direction[2]].has_right_wall = False
                elif random_direction[0] == "Up":
                    self._cells[i][j].has_top_wall = False
                    self._cells[random_direction[1]
                                ][random_direction[2]].has_bottom_wall = False
                else:
                    self._cells[i][j].has_bottom_wall = False
                    self._cells[random_direction[1]
                                ][random_direction[2]].has_top_wall = False

                self._break_walls_r(random_direction[1], random_direction[2])

    def _reset_cells_visited(self):
        for row in self._cells:
            for cell in row:
                cell.visited = False

    def solve(self):
        return self._solve_r(0, 0)

    def check_wall(self, i, j, direction):
        # Left
        if direction[1] == j - 1 and not self._cells[direction[0]][direction[1]].has_right_wall:
            return True
        # Right
        elif direction[1] == j + 1 and not self._cells[direction[0]][direction[1]].has_left_wall:
            return True
        # Up
        elif direction[0] == i - 1 and not self._cells[direction[0]][direction[1]].has_bottom_wall:
            return True
        # Down
        elif direction[0] == i + 1 and not self._cells[direction[0]][direction[1]].has_top_wall:
            return True
        return False

    def _solve_r(self, i, j):
        self._animate()
        directions = [(i, j-1, j - 1 >= 0), (i, j+1, j + 1 < self.num_cols),
                      (i-1, j, i - 1 >= 0), (i+1, j, i + 1 < self.num_rows)]
        self._cells[i][j].visited = True
        if i == self.num_rows-1 and j == self.num_cols-1:
            return True
        for direction in directions:
            if direction[2] and self.check_wall(i, j, direction) and not self._cells[direction[0]][direction[1]].visited:
                self._cells[i][j].draw_move(
                    self._cells[direction[0]][direction[1]])
                if self._solve_r(direction[0], direction[1]):
                    return True
                else:
                    self._cells[i][j].draw_move(
                        self._cells[direction[0]][direction[1]], undo=True)
        return False

    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)
