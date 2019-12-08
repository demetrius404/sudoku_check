import unittest
import app

# add PATH to app.py file
# import sys
# sys.path.append("../")


class TestSudokuCheck(unittest.TestCase):

    def test_grid_ok_1(self):
        grid_test_case = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
                          [6, 7, 2, 1, 9, 5, 3, 4, 8],
                          [1, 9, 8, 3, 4, 2, 5, 6, 7],
                          [8, 5, 9, 7, 6, 1, 4, 2, 3],
                          [4, 2, 6, 8, 5, 3, 7, 9, 1],
                          [7, 1, 3, 9, 2, 4, 8, 5, 6],
                          [9, 6, 1, 5, 3, 7, 2, 8, 4],
                          [2, 8, 7, 4, 1, 9, 6, 3, 5],
                          [3, 4, 5, 2, 8, 6, 1, 7, 9]]
        self.assertEqual(app.sudoku_check(grid_test_case), True)

    def test_grid_ok_2(self):
        grid_test_case = [[4, 1, 6, 7, 5, 8, 2, 3, 9],
                          [8, 7, 9, 4, 2, 3, 1, 5, 6],
                          [3, 5, 2, 1, 9, 6, 7, 8, 4],
                          [1, 3, 5, 8, 7, 9, 6, 4, 2],
                          [6, 2, 8, 3, 1, 4, 5, 9, 7],
                          [9, 4, 7, 2, 6, 5, 3, 1, 8],
                          [2, 8, 3, 5, 4, 7, 9, 6, 1],
                          [5, 6, 1, 9, 8, 2, 4, 7, 3],
                          [7, 9, 4, 6, 3, 1, 8, 2, 5]]
        self.assertEqual(app.sudoku_check(grid_test_case), True)

    def test_grid_ok_3(self):
        grid_test_case = [[7, 4, 6, 9, 3, 2, 1, 5, 8],
                          [8, 9, 1, 6, 4, 5, 3, 7, 2],
                          [2, 3, 5, 8, 1, 7, 4, 6, 9],
                          [3, 6, 9, 5, 2, 4, 7, 8, 1],
                          [4, 7, 2, 1, 8, 9, 5, 3, 6],
                          [5, 1, 8, 7, 6, 3, 2, 9, 4],
                          [1, 5, 7, 2, 9, 6, 8, 4, 3],
                          [9, 2, 3, 4, 7, 8, 6, 1, 5],
                          [6, 8, 4, 3, 5, 1, 9, 2, 7]]
        self.assertEqual(app.sudoku_check(grid_test_case), True)

    def test_grid_er_1(self):
        # bad sum
        grid_test_case = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
                          [6, 7, 2, 1, 9, 5, 3, 4, 8],
                          [1, 9, 8, 3, 4, 2, 5, 6, 7],
                          [8, 5, 9, 7, 6, 1, 4, 2, 3],
                          [4, 2, 6, 8, 5, 6, 7, 9, 1],
                          [7, 1, 3, 9, 2, 4, 8, 5, 6],
                          [9, 6, 1, 5, 3, 7, 2, 8, 4],
                          [2, 8, 7, 4, 1, 9, 6, 3, 5],
                          [3, 4, 5, 2, 8, 6, 1, 7, 9]]
        self.assertEqual(app.sudoku_check(grid_test_case), False)

    def test_grid_er_2(self):
        # bad row and col
        grid_test_case = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
                          [1, 2, 3, 4, 5, 6, 7, 8, 9],
                          [1, 2, 3, 4, 5, 6, 7, 8, 9],
                          [1, 2, 3, 4, 5, 6, 7, 8, 9],
                          [1, 2, 3, 4, 5, 6, 7, 8, 9],
                          [1, 2, 3, 4, 5, 6, 7, 8, 9],
                          [1, 2, 3, 4, 5, 6, 7, 8, 9],
                          [1, 2, 3, 4, 5, 6, 7, 8, 9],
                          [1, 2, 3, 4, 5, 6, 7, 8, 9]]
        self.assertEqual(app.sudoku_check(grid_test_case), False)

    def test_grid_er_3(self):
        # bad element = 0
        grid_test_case = [[4, 1, 6, 7, 5, 8, 2, 3, 9],
                          [8, 7, 9, 4, 2, 3, 1, 5, 6],
                          [3, 5, 2, 1, 9, 6, 7, 8, 4],
                          [1, 3, 5, 8, 7, 9, 6, 4, 2],
                          [6, 2, 8, 3, 1, 4, 5, 9, 7],
                          [9, 4, 7, 2, 6, 0, 3, 1, 8],
                          [2, 8, 3, 5, 4, 7, 9, 6, 1],
                          [5, 6, 1, 9, 8, 2, 4, 7, 3],
                          [7, 9, 4, 6, 3, 1, 8, 2, 5]]
        self.assertEqual(app.sudoku_check(grid_test_case), False)

    def test_grid_er_4(self):
        # bad element = "i"
        grid_test_case = [[4, 1, 6, 7, 5, 8, 2, 3, 9],
                          [8, 7, 9, 4, 2, 3, 1, 5, 6],
                          [3, 5, 2, 1, 9, 6, 7, 8, 4],
                          [1, 3, 5, 8, 7, 9, 6, 4, 2],
                          [6, 2, 8, 3, 1, 4, 5, 9, 7],
                          [9, 4, 7, 2, 6, 5, 3, 1, 8],
                          [2, 8, 3, 5, 4, 7, 9, 6, 1],
                          [5, 6, 1, 9, 8, 2, 4, 7, 3],
                          [7, 9, 4, 6, 3, 1, 8, 2, "i"]]
        self.assertEqual(app.sudoku_check(grid_test_case), False)

    def test_grid_er_5(self):
        # bad sum
        grid_test_case = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
                          [6, 7, 2, 1, 9, 5, 3, 4, 8],
                          [1, 9, 8, 3, 4, 2, 5, 1, 7],
                          [8, 5, 9, 7, 6, 1, 4, 2, 3],
                          [4, 2, 6, 8, 5, 3, 7, 9, 1],
                          [7, 1, 3, 9, 2, 4, 8, 5, 6],
                          [9, 6, 1, 5, 3, 7, 2, 8, 4],
                          [2, 8, 7, 4, 1, 9, 6, 3, 5],
                          [3, 4, 5, 2, 8, 6, 1, 7, 9]]
        self.assertEqual(app.sudoku_check(grid_test_case), False)

    def test_grid_er_6(self):
        # bad shape
        grid_test_case = [[7, 4, 6, 9, 3, 2, 1, 5],
                          [8, 9, 1, 6, 4, 5, 3, 7, 2],
                          [2, 3, 5, 8, 1, 7, 4, 6, 9],
                          [3, 6, 9, 5, 2, 4, 7, 8, 1],
                          [4, 7, 2, 1, 8, 9, 5, 3, 6],
                          [5, 1, 8, 7, 6, 3, 2, 9, 4],
                          [1, 5, 7, 2, 9, 6, 8, 4, 3],
                          [9, 2, 3, 4, 7, 8, 6, 1, 5],
                          [6, 8, 4, 3, 5, 1, 9, 2, 7]]
        self.assertEqual(app.sudoku_check(grid_test_case), False)

    def test_grid_er_7(self):
        # bad shape
        grid_test_case = [[7, 4, 6, 9, 3, 2, 1, 5, 8],
                          [8, 9, 1, 6, 4, 5, 3, 7, 2],
                          [2, 3, 5, 8, 1, 7, 4, 6, 9],
                          [3, 6, 9, 5, 2, 4, 7, 8, 1],
                          [4, 7, 2, 1, 8, 9, 5, 3, 6],
                          [5, 1, 8, 7, 6, 3, 2, 9, 4],
                          [1, 5, 7, 2, 9, 6, 8, 4, 3],
                          [9, 2, 3, 4, 7, 8, 6, 1, 5]]
        self.assertEqual(app.sudoku_check(grid_test_case), False)

    def test_grid_er_8(self):
        # bad shape
        grid_test_case = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
                          [6, 7, 2, 1, 9, 5, 3, 4, 8],
                          [1, 9, 8, 3, 4, 2, 5, 6, 7],
                          [8, 5, 9, 7, 6, 1, 4, 2, 3],
                          [4, 2, 6, 8, 5, 3, 7, 9, 1],
                          [7, 1, 3, 9, 2, 4, 8, 5, 6, 7],
                          [9, 6, 1, 5, 3, 7, 2, 8, 4],
                          [2, 8, 7, 4, 1, 9, 6, 3, 5],
                          [3, 4, 5, 2, 8, 6, 1, 7, 9]]
        self.assertEqual(app.sudoku_check(grid_test_case), False)

    def test_line_ok_1(self):
        grid_test_line = tuple([4, 1, 6, 7, 5, 8, 2, 3, 9])
        self.assertEqual(app.sudoku_line_ok(grid_test_line), True)

    def test_line_ok_2(self):
        grid_test_line = tuple([1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(app.sudoku_line_ok(grid_test_line), True)

    def test_line_er_1(self):
        grid_test_line = tuple([4, 0, 6, 7, 5, 8, 2, 3, 9])
        self.assertEqual(app.sudoku_line_ok(grid_test_line), False)

    def test_line_er_2(self):
        grid_test_line = tuple([4, 1, 6, 7, 5, "h", 2, 3, 9])
        self.assertEqual(app.sudoku_line_ok(grid_test_line), False)

    def test_line_er_3(self):
        grid_test_line = tuple([4, 0, 6, 7, 5, 9, 2, 3, 9])
        self.assertEqual(app.sudoku_line_ok(grid_test_line), False)

    def test_line_er_4(self):
        grid_test_line = tuple([4, 0, 6, 7, 5, 9, 2, 3, 9, 4])
        self.assertEqual(app.sudoku_line_ok(grid_test_line), False)


if __name__ == "__main__":
    unittest.main()
