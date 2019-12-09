import os
import sys

SHAPE_GRID = 9
SHAPE_SQUARE = 3
VALID_ELEMENTS = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# classic sudoku grid 9x9, square 3x3

# deprecated
# def sudoku_element_ok(line: tuple):
#     for element in line:
#         if element not in VALID_ELEMENTS:
#             return False
#     return True


# more beautiful ver of sudoku_element_ok
def sudoku_element_ok_v2(line: tuple):
    line_el = tuple([el for el in line if el in VALID_ELEMENTS])
    return len(line_el) == len(line) 


def sudoku_line_ok(line: tuple):
    if sudoku_element_ok_v2(line) and len(line) == SHAPE_GRID:
        return sum(line) == sum(set(line))
    else:
        return False


def sudoku_square_ok(grid: list):
    squares = []
    grid = list(zip(*grid))
    for i in range(0, SHAPE_GRID, SHAPE_SQUARE):
        for j in range(0, SHAPE_GRID, SHAPE_SQUARE):
            parts_square = list([row[j:j+SHAPE_SQUARE] for row in grid[i:i+SHAPE_SQUARE]])
            square = tuple()
            for part_square in parts_square:
                square += part_square
            squares.append(square)
    return [square for square in squares if not sudoku_line_ok(square)]


def sudoku_shape_ok(grid: list):
    if not len(grid) == SHAPE_GRID:
        return False
    for i in range(0, SHAPE_GRID):
        if not len(grid[i]) == SHAPE_GRID:
            return False
    return True


def sudoku_check(grid: list):
    if not sudoku_shape_ok(grid):
        return False
    bad_rows = [tuple(row) for row in grid if not sudoku_line_ok(tuple(row))]
    bad_cols = [col for col in list(zip(*grid)) if not sudoku_line_ok(col)]
    bad_squares = sudoku_square_ok(grid)
    return not (bad_rows or bad_cols or bad_squares)


def read_from_file(file_name: str):
    grid = []
    if os.path.exists(file_name) and os.path.isfile(file_name):
        with open(file_name, "r", encoding="utf-8") as fs:
            lines = fs.readlines()
    for line in lines:
        grid.append([int(element) for element in line.split(",") if str(element).strip().isdigit()])
    return grid


if __name__ == "__main__":

    GRID = [[4, 1, 6, 7, 5, 8, 2, 3, 9],
            [8, 7, 9, 4, 2, 3, 1, 5, 6],
            [3, 5, 2, 1, 9, 6, 7, 8, 4],
            [1, 3, 5, 8, 7, 9, 6, 4, 2],
            [6, 2, 8, 3, 1, 4, 5, 9, 7],
            [9, 4, 7, 2, 6, 5, 3, 1, 8],
            [2, 8, 3, 5, 4, 7, 9, 6, 1],
            [5, 6, 1, 9, 8, 2, 4, 7, 3],
            [7, 9, 4, 6, 3, 1, 8, 2, 5]]

    print("sudoku valid:", sudoku_check(GRID))

    if len(sys.argv) == 2:
        print("load from file:", sys.argv[1])
        print("sudoku valid:", sudoku_check(read_from_file(sys.argv[1])))
