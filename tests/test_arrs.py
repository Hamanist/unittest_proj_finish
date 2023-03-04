import unittest
from utils import arrs


class TestArrs(unittest.TestCase):

    def test_get_normal(self):
        self.assertEqual(arrs.get([1, 2, 3], 2, "test"), 3)

    def test_get_index_less_than_zero(self):
        self.assertEqual(arrs.get([], -1, "test"), "test")

    def test_get_error(self):
        with self.assertRaises(IndexError):
            arrs.get([], 0, "test")

    def test_slice_normal(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], 1), [2, 3])

    def test_slice_if_the_list_is_empty(self):
        self.assertEqual(arrs.my_slice([]), [])

    def test_slice_start_less_length_list(self):
        self.assertEqual(arrs.my_slice([1, 2, 3], -5, 2), [1, 2])

    def test_slice_normalized_start(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], -3, 3), [2, 3])
