SHAPE = 9


def sudoku_element_ok(line: tuple):
    valid_elements = (1, 2, 3, 4, 5, 6, 7, 8, 9)
    for element in line:
        if element not in valid_elements:
            return False
    return True


def sudoku_line_ok(line: tuple):
    if sudoku_element_ok(line) and len(line) == SHAPE:
        return sum(line) == sum(set(line))
    else:
        return False


def sudoku_square_ok(grid: list):
    squares = []
    grid = list(zip(*grid))
    for i in range(0, SHAPE, 3):
        for j in range(0, SHAPE, 3):
            parts_square = list([row[j:j+3] for row in grid[i:i+3]])
            square = tuple()
            for part_square in parts_square:
                square += part_square
            squares.append(square)
    return [square for square in squares if not sudoku_line_ok(square)]


def sudoku_shape_ok(grid: list):
    if not len(grid) == SHAPE:
        return False
    for i in range(0, SHAPE):
        if not len(grid[i]) == SHAPE:
            return False
    return True


def sudoku_check(grid: list):
    if not sudoku_shape_ok(grid):
        return False
    bad_rows = [tuple(row) for row in grid if not sudoku_line_ok(tuple(row))]
    bad_cols = [col for col in list(zip(*grid)) if not sudoku_line_ok(col)]
    bad_squares = sudoku_square_ok(grid)
    return not (bad_rows or bad_cols or bad_squares)


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

