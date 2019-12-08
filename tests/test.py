import unittest
import app


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

    def test_grid_er_1(self):
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

    def test_line_ok_1(self):
        grid_test_line = [4, 1, 6, 7, 5, 8, 2, 3, 9]
        self.assertEqual(app.sudoku_line_ok(grid_test_line), True)

    def test_line_er_1(self):
        grid_test_line = [4, 0, 6, 7, 5, 8, 2, 3, 9]
        self.assertEqual(app.sudoku_line_ok(grid_test_line), False)

    def test_line_er_2(self):
        grid_test_line = [4, 1, 6, 7, 5, "i", 2, 3, 9]
        self.assertEqual(app.sudoku_line_ok(grid_test_line), False)

    def test_line_er_3(self):
        grid_test_line = [4, 0, 6, 7, 5, 9, 2, 3, 9]
        self.assertEqual(app.sudoku_line_ok(grid_test_line), False)


if __name__ == "__main__":
    unittest.main()