#!/usr/bin/env python


class Node:
    def __init__(self, data):
        self.data = data  # Assign node data
        self.next = None  # Initialize next node as null
    
    def __repr__(self):
        return "Node({})".format(self.data)


class LinkedList:
    def __init__(self):
        self.head = None  # Initialize Linked List object

    def _print(self):
        node = self.head  # Start from head

        while node:
            print(node.data)
            # After print node data, shift cursor to next node
            node = node.next

    def push(self, data):
        """Insert a new node at the beginning of Linked List."""
        node = Node(data)  # Allocate the Node and put it the data
        node.next = self.head  # Make the head, as the next of node
        self.head = node  # Move the head to point of the new Node

    def insert_after(self, previous, data):
        """Insert a new node after the given previous node."""

        # check if the given node (previous) exists
        if previous is None:
            print("The given previous node must be in Linked List")
            return

        node = Node(data)
        node.next = previous.next  # Make the next of new Node as next of previous
        previous.next = node  # Make the next of previous as node

    def append(self, data):
        """Append a new node at the end of Linked List."""
        node = Node(data)

        if self.head is None:  # If LL is empty, the new node is head.
            self.head = node
            return

        last = self.head

        while (last.next):  # Traverse all the LL until last node
            last = last.next

        last.next = node  # Then, set last node as appended node

    def delete(self, data):
        """Delete the firts node found matching th data."""
        node = self.head

        if node is not None:  # If head holds the data, then delete it
            if node.data == data:
                self.head = node.next
                node = None
                return

        while node is not None:  # Search for data
            if node.data == data:  # Found the data
                break
            previous = node  # Keep the track of node
            node = node.next

        if node == None:  # Key not found
            return

        previous.next = node.next  # Unlink node from LL

        node = None

    def reverse(self):
        """Reverese the Linked List."""
        previous = None
        current = self.head

        while current is not None:
            next = current.next
            current.next = previous
            previous = current
            current = next
        self.head = previous

