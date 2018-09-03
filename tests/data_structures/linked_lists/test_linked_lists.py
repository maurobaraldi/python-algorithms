#!/usr/bin/env python

import unittest
from data_structures.linked_lists.linked_lists import Node, LinkedList


class TestNode(unittest.TestCase):

   def test_define_a_node(self):
        node = Node(1)

        self.assertIsInstance(node, Node)
        self.assertEqual(node.data, 1)


class TestLinkdeList(unittest.TestCase):

    def test_instantiate_a_linked_list(self):
        linkedl = LinkedList()
        linkedl.head = Node(1)

        self.assertIsInstance(linkedl, LinkedList)
        self.assertEqual(linkedl.head.data, 1)

    def test_instantiate_a_linked_list_with_three_nodes(self):
        linkedl = LinkedList()

        first = Node(1)
        second = Node(2)
        third = Node(3)

        linkedl.head = first
        linkedl.head.next = second

        second.next = third

        self.assertEqual(linkedl.head.data, 1)
        self.assertEqual(linkedl.head.next.data, 2)
        self.assertEqual(linkedl.head.next.next.data, 3)

    def test_push_node_to_linked_list(self):
        linked_list = LinkedList()

        linked_list.head = Node(1)
        linked_list.push(2)

        self.assertEqual(linked_list.head.data, 2)
        self.assertEqual(linked_list.head.next.data, 1)

    def test_insert_after_node_in_linked_list(self):
        linked_list = LinkedList()

        linked_list.head = Node(1)
        linked_list.head.next = Node(2)
        linked_list.insert_after(linked_list.head, 3)
        linked_list._print()

        self.assertEqual(linked_list.head.data, 1)
        self.assertEqual(linked_list.head.next.data, 3)
        self.assertEqual(linked_list.head.next.next.data, 2)

    def test_append_node_to_linked_list(self):
        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(3)
        linked_list.append(6)

        self.assertEqual(linked_list.head.data, 1)
        self.assertEqual(linked_list.head.next.data, 3)
        self.assertEqual(linked_list.head.next.next.data, 6)

    def test_delete_node_from_linked_list(self):
        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)
        linked_list.delete(2)

        self.assertEqual(linked_list.head.data, 1)
        self.assertEqual(linked_list.head.next.data, 3)
 
    def test_reverse_a_linked_list(self):
        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)
        linked_list.reverse()

        self.assertEqual(linked_list.head.data, 3)
        self.assertEqual(linked_list.head.next.next.data, 1)
 
