#!/usr/bin/env python

import unittest
from algorithms.sets.longest_common_subsequence import lcs


class TestShuffle(unittest.TestCase):

    def test_lcs_computation(self):
        self.assertEqual(lcs.lcs([], []), "")
        self.assertEqual(lcs.lcs('gratitude', 'intention'), "ite")
        self.assertEqual(lcs.lcs('GAC', 'AGACT'), "GAC")

    def test_lcs_computation_recursive(self):
        self.assertEqual(lcs.lcs_recursive([], []), "")
        self.assertEqual(lcs.lcs_recursive('gratitude', 'intention'), "ite")
        self.assertEqual(lcs.lcs_recursive('GAC', 'AGACT'), "GAC")

if __name__ == '__main__':
    unittest.main()
