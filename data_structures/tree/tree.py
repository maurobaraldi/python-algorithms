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

    def add(self, value, node=None):
        """Add new node to tree (recursively)."""
        if node is None:
            node = self.root

        if self.root is None:
            self.root = Node(value)

        else:

            if value <= node.value:  # Go to branch / of tree.

                if node.left is not None:  # This node, already has a node.
                    self.add(value, node.left)  # Re-call add new node mehtod.
                else:
                    node.left = Node(value)  # node is None, add new node.

            else:

                if node.right is not None:
                    self.add(value, node.right)
                else:
                    node.right = Node(value)

    def search(self, value, node=None):
        """Search for node containing value (recursively)."""
        if node is None:
            node = self.root

        if self.root.value == value:
            return self.root

        else:

            if node.value == value:
                return node

            if node.value > value and node.left is not None:
                return self.search(value, node.left)

            if node.value < value and node.right is not None:
                return self.search(value, node.right)

            return None

    def delete(self, value, node=None):
        """
        Delete node by key.

        Cases:
        1 - Value to be deleted is smaller than root's value.
        2 - Value to be deleted is greateer than root's value.
        3 - Node with no child or just one child (left or right).
        """
        if node is None:  # node if unknow, so search by key, and define a node.
            node = self.search(value)

        # Case 1
        if value < node.value:
            node.left = self.delete(value, node.left)

        # Case 2
        elif value > node.value:
            node.right = self.delete(value, node.right)

        else:

            if node.left is None:
                n = node.right
                node = None
                return n
            elif node.right is None:
                n = node.left
                node = None
                return n




    def traverse(self, node):
        """Traverse tree and print each item."""

        if node is not None:
            self.traverse(node.left)  # Recursive traverse.
            print(node.value)
            self.traverse(node.right)

