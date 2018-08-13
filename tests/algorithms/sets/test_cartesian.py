#!/usr/bin/env python

import unittest
from algorithms.sets.cartesian_product import cartesian


class TestFatorial(unittest.TestCase):

    def setUp(self):
        self.set_a = [1, 2]
        self.set_b = [4, 5]

    def test_cartesian_product(self):
        self.assertEqual(cartesian.product(self.set_a, self.set_b), [[1, 4], [1, 5], [2, 4], [2, 5]])

    def test_cartesian_product_by_list_comprehension(self):
        self.assertEqual(cartesian.list_comprehension(self.set_a, self.set_b), [[1, 4], [1, 5], [2, 4], [2, 5]])

    def test_cartesian_product_recursive_two_sets(self):
        result = [i for i in cartesian.product_n(self.set_a, self.set_b)]
        self.assertEqual(result, [[1, 4], [1, 5], [2, 4], [2, 5]])

    def test_cartesian_product_recursive_three_sets(self):
        result = [i for i in cartesian.product_n(self.set_a, self.set_b, self.set_a)]
        self.assertEqual(result, [[1, 4, 1], [1, 4, 2], [1, 5, 1], [1, 5, 2], [2, 4, 1], [2, 4, 2], [2, 5, 1], [2, 5, 2]])


if __name__ == '__main__':
    unittest.main()
