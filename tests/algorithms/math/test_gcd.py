#!/usr/bin/env python

import unittest
from algorithms.math.gcd import gcd


class TestFatorial(unittest.TestCase):

    def test_gcd_using_recursive(self):
        self.assertEqual(gcd.gcd_recursive(4, 2), 2)
        self.assertEqual(gcd.gcd_recursive(252, 105), 21)
        self.assertEqual(gcd.gcd_recursive(1386, 3213), 63)

    def test_gcd_using_sub(self):
        self.assertEqual(gcd.gcd_sub(4, 2), 2)
        self.assertEqual(gcd.gcd_sub(252, 105), 21)
        self.assertEqual(gcd.gcd_sub(1386, 3213), 63)

    def test_gcd_using_mod(self):
        self.assertEqual(gcd.gcd_mod(4, 2), 2)
        self.assertEqual(gcd.gcd_mod(252, 105), 21)
        self.assertEqual(gcd.gcd_mod(1386, 3213), 63)

if __name__ == '__main__':
    unittest.main()
