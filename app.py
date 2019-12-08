def sudoku_element_ok(line: tuple):
    valid_elements = (1, 2, 3, 4, 5, 6, 7, 8, 9)
    for element in line:
        if element not in valid_elements:
            return False
    return True


def sudoku_line_ok(line: tuple):
    if sudoku_element_ok(line) and len(line) == 9:
        return sum(line) == sum(set(line))
    else:
        return False


def sudoku_check(grid):
    bad_rows = [row for row in grid if not sudoku_line_ok(tuple(row))]
    grid = list(zip(*grid))
    bad_cols = [col for col in grid if not sudoku_line_ok(col)]
    squares = []
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            parts_square = list([row[j:j+3] for row in grid[i:i+3]])
            square = tuple()
            for part_square in parts_square:
                square += part_square
            squares.append(square)
    bad_squares = [square for square in squares if not sudoku_line_ok(square)]
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

