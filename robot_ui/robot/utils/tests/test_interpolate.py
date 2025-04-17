import unittest
import numpy as np
from robot.utils.interpolate import get_interpolated_matrix_data


class TestInterpolation(unittest.TestCase):
    def test_returns_20_matrices(self):
        start = [0, 0, 0, 0, 0, 0]
        end = [90, 90, 90, 90, 90, 90]
        robot_params_a = [10, 20, 10, 30, 10, 5]
        robot_params_d = [10, 20, 10, 30, 10, 5]
        result = get_interpolated_matrix_data(start, end, robot_params_a, robot_params_d)
        self.assertEqual(len(result), 20)
        for matrix in result:
            self.assertEqual(len(matrix), 4)  # 4 rows
            for row in matrix:
                self.assertEqual(len(row), 4)  # 4 columns


if __name__ == "__main__":
    unittest.main()
