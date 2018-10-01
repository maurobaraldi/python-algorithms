#!/usr/bin/env python

import unittest
from algorithms.compression.rle import rle


class TestRunLengthEncoding(unittest.TestCase):

    def test_encoding(self):
        self.assertEqual(rle.encode("aaaabbbbbbccccccddddddeeeeeefff"), "4a6b6c6d6e3f")

    def test_decoding(self):
        self.assertEqual(rle.decode("4a6b6c6d6e3f"), "aaaabbbbbbccccccddddddeeeeeefff")

if __name__ == '__main__':
    unittest.main()
