#!/usr/bin/env python

import unittest
from data_structures.stack.stack import (
        Stack,
        EmptyStackError,
        FullStackError
)


class TestStack(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()

    def test_define_a_stack(self):
        self.assertIsInstance(self.stack, Stack)

    def test_if_stack_is_empty(self):
        self.assertTrue(self.stack.is_empty())

    def test_if_stack_is_not_empty(self):
        self.stack.push(1)

        self.assertFalse(self.stack.is_empty())

    def test_add_element_to_stack(self):
        self.stack.push(1)

        self.assertEquals(self.stack.stack, [1])

    def test_add_element_to_an_fulfilled_stack(self):
        self.stack.push(1)

        with self.assertRaises(FullStackError):
            self.stack.push(2)

    def test_pop_an_element_to_stack(self):
        self.stack.push(1)
        element = self.stack.pop()

        self.assertEquals(element, 1)

    def test_pop_an_element_from_empty_stack(self):
        with self.assertRaises(EmptyStackError):
            self.stack.pop()

    def test_peek_an_element_from_stack(self):
        self.stack.max_size = 2  # Patch object's capacity
        self.stack.push(1)
        self.stack.push(2)
        element = self.stack.peek()

        self.assertEquals(element, 2)

    def test_peek_an_element_from_empty_stack(self):
        with self.assertRaises(EmptyStackError):
            self.stack.peek()

    def test_get_size_if_stack(self):
        self.stack.push(1)

        self.assertEquals(self.stack.size(), 1)


