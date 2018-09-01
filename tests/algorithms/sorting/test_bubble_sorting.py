#!/usr/bin/env python

import unittest
from algorithms.sorting.bubble_sort import bubble


class TestiBubble(unittest.TestCase):
    def setUp(self):
        self.sorted = [1,2,3,4,5]
        self.unsorted = [2, 5, 3, 1, 4]

    def test_naive_soluion(self):
        self.assertEqual(bubble.naive([1]), [1])
        self.assertEqual(bubble.naive(self.sorted), [1,2,3,4,5])
        self.assertEqual(bubble.naive(self.unsorted), [1,2,3,4,5])


    def test_improved_soluion(self):
        self.assertEqual(bubble.improved([1]), [1])
        self.assertEqual(bubble.improved(self.sorted), [1,2,3,4,5])
        self.assertEqual(bubble.improved(self.unsorted), [1,2,3,4,5])

    def test_recursive_soluion(self):
        self.assertEqual(bubble.recursive([1]), [1])
        self.assertEqual(bubble.recursive(self.sorted), [1,2,3,4,5])
        self.assertEqual(bubble.recursive(self.unsorted), [1,2,3,4,5])
