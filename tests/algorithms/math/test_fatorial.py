#!/usr/bin/env python

import unittest
from algorithms.math.fatorial import fatorial

class TestFatorial(unittest.TestCase):

    def test_fatorial_for(self):
        self.assertEqual(fatorial.fatorial_1(1), 1)
        self.assertEqual(fatorial.fatorial_1(3), 6)
        self.assertEqual(fatorial.fatorial_1(5), 120)

    def test_fatorial_while(self):
        self.assertEqual(fatorial.fatorial_2(1), 1)
        self.assertEqual(fatorial.fatorial_2(3), 6)
        self.assertEqual(fatorial.fatorial_2(5), 120)

    def test_fatorial_recursive(self):
        self.assertEqual(fatorial.fatorial_3(1), 1)
        self.assertEqual(fatorial.fatorial_3(3), 6)
        self.assertEqual(fatorial.fatorial_3(5), 120)

if __name__ == '__main__':
    unittest.main()
