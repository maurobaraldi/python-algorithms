#!/usr/bin/env python

import unittest
from algorithms.sorting.selection_sort import selection


class TestSelectionSort(unittest.TestCase):
    def setUp(self):
        self.sorted = [1,2,3,4,5]
        self.unsorted = [2, 5, 3, 1, 4]

    def test_naive_solution(self):
        self.assertEqual(selection.sort([1]), [1])
        self.assertEqual(selection.sort(self.sorted), [1,2,3,4,5])
        self.assertEqual(selection.sort(self.unsorted), [1,2,3,4,5])

    def test_recursive_solution(self):
        self.assertEqual(selection.recursive([1], 1), [1])
        self.assertEqual(selection.recursive(self.sorted, 5), [1,2,3,4,5])
        self.assertEqual(selection.recursive(self.unsorted, 5), [1,2,3,4,5])

