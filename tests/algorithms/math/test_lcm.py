#!/usr/bin/env python

import unittest
from algorithms.math.lcm import lcm

class TestFatorial(unittest.TestCase):

    def test_lcm_brute_force(self):
        self.assertEqual(lcm.lcm(2, 4), 4)
        self.assertEqual(lcm.lcm(2, 3), 6)
        self.assertEqual(lcm.lcm(2, 5), 10)
        self.assertEqual(lcm.lcm(2, 10), 10)
        self.assertNotEqual(lcm.lcm(2, 10), 100)

    def test_lcm_by_gcd(self):
        self.assertEqual(lcm.lcm_by_gcd(2, 4), 4)
        self.assertEqual(lcm.lcm_by_gcd(2, 3), 6)
        self.assertEqual(lcm.lcm_by_gcd(2, 5), 10)
        self.assertEqual(lcm.lcm_by_gcd(2, 10), 10)
        self.assertNotEqual(lcm.lcm_by_gcd(2, 10), 100)

if __name__ == '__main__':
    unittest.main()
