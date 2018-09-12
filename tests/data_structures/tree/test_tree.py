#!/usr/bin/env python

import contextlib
import unittest
from io import StringIO
from data_structures.tree.tree import Node, BinarySearchTree


class TestNode(unittest.TestCase):

   def test_define_a_node(self):
        node = Node(1)

        self.assertIsInstance(node, Node)
        self.assertEqual(node.value, 1)

   def test_define_a_right_node(self):
        node = Node(1)
        node.right = Node(2)

        self.assertEqual(node.right.value, 2)

   def test_define_a_left_node(self):
        node = Node(2)
        node.left = Node(1)

        self.assertEqual(node.left.value, 1)

   def test_define_left_and_right_nodes(self):
        node = Node(2)
        node.left = Node(1)
        node.right = Node(3)

        self.assertEqual(node.left.value, 1)
        self.assertEqual(node.right.value, 3)

class TestBnarySearchTree(unittest.TestCase):

    def test_define_a_tree(self):
        tree = BinarySearchTree()

        self.assertIsInstance(tree, BinarySearchTree)

    def test_add_one_item_to_tree(self):
        tree = BinarySearchTree()
        tree.add(10)

        self.assertEqual(tree.root.value, 10)

    def test_add_one_item_smaller_than_root(self):
        tree = BinarySearchTree()
        tree.add(10)
        tree.add(5)

        self.assertEqual(tree.root.value, 10)
        self.assertEqual(tree.root.left.value, 5)

    def test_add_one_item_greater_than_root(self):
        tree = BinarySearchTree()
        tree.add(10)
        tree.add(15)

        self.assertEqual(tree.root.value, 10)
        self.assertEqual(tree.root.right.value, 15)

    def test_add_items_to_tree(self):
        tree = BinarySearchTree()
        tree.add(10)
        tree.add(15)
        tree.add(5)
        tree.add(1)
        tree.add(17)

        self.assertEqual(tree.root.value, 10)
        self.assertEqual(tree.root.right.value, 15)
        self.assertEqual(tree.root.left.value, 5)
        self.assertEqual(tree.root.left.left.value, 1)
        self.assertEqual(tree.root.right.right.value, 17)

    def test_traverse_tree(self):
        tree = BinarySearchTree()
        tree.add(10)
        tree.add(15)
        tree.add(5)
        tree.add(1)
        tree.add(17)

        stdout = StringIO()

        with contextlib.redirect_stdout(stdout):
            tree.traverse(tree.root)

        self.assertEqual(stdout.getvalue().strip(), "1\n5\n10\n15\n17")

    def test_find_in_tree(self):
        tree = BinarySearchTree()
        tree.add(10)
        tree.add(15)
        tree.add(5)
        tree.add(1)
        tree.add(17)

        self.assertEqual(tree.find(5), 5)

