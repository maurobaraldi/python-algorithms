#!/usr/bin/env python3


class Node:
    """Individual node in tree."""
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def __repr__(self):
        return "{}".format(self.value)

class BinarySearchTree:
    """Basic implementation of a Binary Search Tree."""
    def __init__(self):
        self.root = None

    def add(self, value):
        """Add new node to tree."""
        if self.root is None:
            self.root = Node(value)
        else:
            self.__add__(self.root, value)

    def __add__(self, node, value):
        """Recursive adding feature to tree."""
        if value <= node.value:  # Go to branch / of tree.
            if node.left is not None:  # This node, already has a node.
                self.__add__(node.left, value)  # Re-call add new node mehtod.
            else:
                node.left = Node(value)  # Finally, add new node.
        else:  # Go to branch \ of tree.
            if node.right is not None:
                self.__add__(node.right, value)
            else:
                node.right = Node(value)

    def traverse(self, node):
        """Traverse tree and print each item."""

        if node is not None:
            self.traverse(node.left)  # Recursive traverse.
            print(node.value)
            self.traverse(node.right)

    def find(self, value):
        """Find node having given value."""

        if self.root is not None:  # Tree is not empty
            return self.__find__(value, self.root)  # Find through tree.
        return None

    def __find__(self, value, node):
        """Recursive finding feature trough tree."""
        if value == node.value:
            return node
        if value < node.value and node.left is not None:
            return self.__find__(value, node.left)
        if value > node.value and node.right is not None:
            return self.__find__(value, node.right)

