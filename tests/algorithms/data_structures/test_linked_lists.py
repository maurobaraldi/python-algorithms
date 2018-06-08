#!/usr/bin/env python

import unittest
from algorithms.data_structures.linked_lists.simple_linked_list import SimpleLinkedList


class TestSimpleLinkedList(unittest.TestCase):

    def setUp(self):
        self.list = SimpleLinkedList()

    def tearDown(self):
        self.list = None

    def test_prepend_to_empty_list(self):
        self.list.prepend(1)
        self.assertEqual(self.list.head.data, 1)
        self.assertEqual(self.list.tail, None)

    def test_prepend_to_not_empty_list(self):
        self.list.prepend(2)
        self.list.prepend(1)
        self.assertEqual(self.list.head.data, 1)
        self.assertEqual(self.list.tail.data, 2)

    def test_append_append_to_empty_list(self):
        self.list.append(1)
        self.assertEqual(self.list.head.data, 1)

    def test_append_append_to_not_empty_list(self):
        self.list.append(1)
        self.list.append(2)
        self.list.append(3)
        self.assertEqual(self.list.head.data, 1)
        self.assertEqual(self.list.tail.data, 3)

    def test_count_empty_list(self):
        self.assertEqual(self.list.length(), 0)

    def test_count_list_items(self):
        self.list.append(1)
        self.list.append(2)
        self.list.append(3)
        self.assertEqual(self.list.length(), 3)

    def test_pop_from_empty_list(self):
        self.assertEqual(self.list.pop(), None)

    def test_pop_from_list(self):
        self.list.append(1)
        self.list.append(2)
        self.list.append(3)
        self.assertEqual(self.list.pop(), 3)
        self.assertEqual(self.list.tail.data, 2)

    def test_get_index_from_item_in_list(self):
        self.list.append(1)
        self.list.append(2)
        self.list.append(3)
        self.assertEqual(self.list.index(2), 1)

if __name__ == '__main__':
    unittest.main()
