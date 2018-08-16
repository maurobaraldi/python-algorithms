#!/usr/bin/env python

import unittest
from algorithms.sets.combinations import permutations


class TestFatorial(unittest.TestCase):

    def test_permutations_recursive(self):
        self.assertEqual(permutations.permutation([]), [])
        self.assertEqual(permutations.permutation([1]), [[1]])
        self.assertEqual(permutations.permutation([1, 2, 3]), [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]])

    def test_permutations_no_recursion(self):
        self.assertEqual(permutations.permutation_non_recursion([]), [])
        self.assertEqual(permutations.permutation_non_recursion([1]), [1])
        self.assertEqual(permutations.permutation_non_recursion([1, 2]), [[1, 2], [2, 1]])
        self.assertEqual(permutations.permutation_non_recursion([1, 2, 3]), [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]])
