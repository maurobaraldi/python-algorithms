#!/usr/bin/env python

import unittest
from algorithms.math.primes import primes

class TestFatorial(unittest.TestCase):

    def test_primality_by_six_k_form(self):
        self.assertFalse(primes.six_k_form(1))
        self.assertTrue(primes.six_k_form(2))
        self.assertTrue(primes.six_k_form(3))
        self.assertFalse(primes.six_k_form(4))
        self.assertTrue(primes.six_k_form(5))
        self.assertFalse(primes.six_k_form(6))
        self.assertTrue(primes.six_k_form(7))
        self.assertFalse(primes.six_k_form(8))
        self.assertFalse(primes.six_k_form(9))
        self.assertFalse(primes.six_k_form(10))
        self.assertTrue(primes.six_k_form(11))
        self.assertTrue(primes.six_k_form(7919))

    def test_primality_by_agk_form(self):
        self.assertTrue(primes.agk_form(1))
        self.assertTrue(primes.agk_form(2))
        self.assertTrue(primes.agk_form(3))
        self.assertFalse(primes.agk_form(4))
        self.assertTrue(primes.agk_form(5))
        self.assertFalse(primes.agk_form(6))
        self.assertTrue(primes.agk_form(7))
        self.assertFalse(primes.agk_form(8))
        self.assertFalse(primes.agk_form(9))
        self.assertFalse(primes.agk_form(10))
        self.assertTrue(primes.agk_form(11))
        self.assertTrue(primes.agk_form(7919))

    def test_primality_by_little_fermat_form(self):
        self.assertFalse(primes.little_fermat_form(1, 1))
        self.assertTrue(primes.little_fermat_form(2, 1))
        self.assertTrue(primes.little_fermat_form(3, 1))
        self.assertFalse(primes.little_fermat_form(4, 1))
        self.assertTrue(primes.little_fermat_form(5, 2))
        self.assertFalse(primes.little_fermat_form(6, 5))
        self.assertTrue(primes.little_fermat_form(7, 6))
        self.assertFalse(primes.little_fermat_form(8, 7))
        self.assertFalse(primes.little_fermat_form(9, 8))
        self.assertFalse(primes.little_fermat_form(10, 5))
        self.assertTrue(primes.little_fermat_form(11, 6))
        self.assertTrue(primes.little_fermat_form(7919, 200))

    def test_primality_by_sieve_of_erastosthenes(self):
        self.assertEqual(primes.sieve_of_erastosthenes(5), [2, 3])
        self.assertEqual(primes.sieve_of_erastosthenes(10), [2, 3, 5, 7])
        self.assertEqual(primes.sieve_of_erastosthenes(20), [2, 3, 5, 7, 11, 13, 17, 19])


if __name__ == '__main__':
    unittest.main()
