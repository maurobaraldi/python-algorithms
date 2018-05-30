#!/usr/bin/env python

import unittest
import fibonacci


class TestFibonacci(unittest.TestCase):

    def test_fibonacci_recursive(self):
        self.assertEqual(fibonacci.fibonacci_recursive(1), 1)
        self.assertEqual(fibonacci.fibonacci_recursive(2), 1)
        self.assertEqual(fibonacci.fibonacci_recursive(3), 2)
        self.assertEqual(fibonacci.fibonacci_recursive(4), 3)
        self.assertEqual(fibonacci.fibonacci_recursive(5), 5)
        self.assertEqual(fibonacci.fibonacci_recursive(6), 8)
        self.assertEqual(fibonacci.fibonacci_recursive(7), 13)
        self.assertEqual(fibonacci.fibonacci_recursive(8), 21)
        self.assertEqual(fibonacci.fibonacci_recursive(9), 34)
        self.assertEqual(fibonacci.fibonacci_recursive(10), 55)

    def test_fibonacci_for(self):
        self.assertEqual(fibonacci.fibonacci_for(1), 1)
        self.assertEqual(fibonacci.fibonacci_for(2), 1)
        self.assertEqual(fibonacci.fibonacci_for(3), 2)
        self.assertEqual(fibonacci.fibonacci_for(4), 3)
        self.assertEqual(fibonacci.fibonacci_for(5), 5)
        self.assertEqual(fibonacci.fibonacci_for(6), 8)
        self.assertEqual(fibonacci.fibonacci_for(7), 13)
        self.assertEqual(fibonacci.fibonacci_for(8), 21)
        self.assertEqual(fibonacci.fibonacci_for(9), 34)
        self.assertEqual(fibonacci.fibonacci_for(10), 55)


if __name__ == '__main__':
    unittest.main()
