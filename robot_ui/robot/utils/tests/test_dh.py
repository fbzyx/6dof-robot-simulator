import unittest
import numpy as np
from numpy.testing import assert_array_almost_equal
from robot.utils.dh import dh_transform, forward_kinematics


class TestDHTransform(unittest.TestCase):
    def test_identity_transform(self):
        a, alpha, d, theta = 0, 0, 1, 0
        expected = np.array(
            [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 1], [0, 0, 0, 1]]
        )
        result = dh_transform(a, alpha, d, theta)
        assert_array_almost_equal(result, expected, decimal=6)

    def test_90_degree_rotation(self):
        a, alpha, d, theta = 1, 0, 0, np.pi / 2
        expected = np.array(
            [[0, -1, 0, 0], [1, 0, 0, 1], [0, 0, 1, 0], [0, 0, 0, 1]]
        )
        result = dh_transform(a, alpha, d, theta)
        assert_array_almost_equal(result, expected, decimal=6)

    def test_link_twist(self):
        a, alpha, d, theta = 0, np.pi / 2, 0, 0
        expected = np.array(
            [[1, 0, 0, 0], [0, 0, -1, 0], [0, 1, 0, 0], [0, 0, 0, 1]]
        )
        result = dh_transform(a, alpha, d, theta)
        assert_array_almost_equal(result, expected, decimal=6)


if __name__ == "__main__":
    unittest.main()
