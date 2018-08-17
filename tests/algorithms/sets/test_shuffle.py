#!/usr/bin/env python

import unittest
from algorithms.sets.shuffle import shuffle


class TestShuffle(unittest.TestCase):

    def test_sattolo_shuffle(self):
        self.assertEqual(shuffle.sattolo([]), [])
        self.assertEqual(shuffle.sattolo([1]), [1])
        # This test is deterministic
        self.assertNotEqual(shuffle.sattolo([2, 1, 3]), [2, 3, 1])

    def test_fisher_yates_shuffle(self):
        self.assertEqual(shuffle.fisher_yates([]), [])
        self.assertEqual(shuffle.fisher_yates([1]), [1])
        # This test is deterministic
        self.assertNotEqual(shuffle.fisher_yates([2, 1, 3]), [2, 3, 1])

if __name__ == '__main__':
    unittest.main()
