#!/usr/bin/env python

import unittest
from data_structures.linked_lists.doubly_linked_lists import (
    Node,
    DoublyLinkedList
)


class TestNode(unittest.TestCase):

    def test_define_a_node(self):
        node = Node(1)

        self.assertIsInstance(node, Node)
        self.assertEqual(node.data, 1)


class TestDoublyLinkdeList(unittest.TestCase):
    def setUp(self):
        self.node = Node(1)
        self.dll = DoublyLinkedList()

    def test_instantiate_a_doubly_linked_list(self):
        self.dll.head = self.node

        self.assertIsInstance(self.dll, DoublyLinkedList)
        self.assertEqual(self.dll.head.data, 1)

    def test_push_node_to_doubly_linked_list(self):
        self.dll.push(1)
        self.dll.push(2)

        self.assertEqual(self.dll.head.next.data, 1)
        self.assertEqual(self.dll.head.next.prev.data, 2)

    def test_append_node_to_doubly_linked_list(self):
        self.dll.append(6)
        self.dll.append(1)
        self.dll.append(3)
        self.dll.append(2)

        self.assertEqual(self.dll.head.data, 6)
        self.assertEqual(self.dll.head.next.data, 1)
        self.assertEqual(self.dll.tail.data, 2)

    def test_delete_node_to_doubly_linked_list(self):
        self.dll.append(6)
        self.dll.append(1)
        self.dll.remove(6)

        self.assertEqual(self.dll.head.data, 1)
