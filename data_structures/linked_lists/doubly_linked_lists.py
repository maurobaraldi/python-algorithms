#!/usr/bin/env python3


class Node:
    def __init__(self, data):
        self.data = data  # Assign node data
        self.next = None  # Initialize next node as null
        self.prev = None  # Initialize previous node as null


class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Initialize Doubly Linked List object

    def push(self, data):
        """Insert a new node at the beginning of DLL."""
        node = Node(data)  # Allocate the Node and put it the data
        node.next = self.head  # Make the head, as the next of node

        if self.head is not None:  # Change prev of head node to new_node
            self.head.prev = node

        self.head = node  # Move the head to point to the new node

    def insert_after(self, previous, data):
        """Insert a new node after the given previous node."""

        # check if the given node (previous) exists
        if previous is None:
            print("The given previous node must be in Linked List")
            return

        node = Node(data)
        node.next = previous.next  # Make the next of new Node as next of previous
        previous.next = node  # Make the next of previous as node
        node.prev = previous  # Make the `previous` as the previous of new_node

        if node.next != None:  # Change previous of node's next node
            node.next.prev = node

    def append(self, data):
        """Append a new node at the end of Doubly Linked List."""
        node = Node(data)
        last = self.head
        node.next = None

        if self.head is None:  # If DLL is empty, the new node is head.
            node.prev = None
            self.head = node
            return

        while last.next != None:  # Traverse all the DLL until last node
            last = last.next

        last.next = node  # Then, set last node as appended node
        node.prev = last  # Make the last node as previous of (new) node

    def insert_before(self, next, data):
        """Insert a new node before the given node."""

        # check if the given node (previous) exists
        if next is None:
            print("The given previous node must be in Linked List")
            return

        node = Node(data)
        node.prev = next.prev  # Make the previous of new Node as the previous of next
        next.prev = node  # Make the prev of next Node as new Node (node)
        node.next = node  # Make the next Node as next of new Node (node)

        if node.prev != None:  # Change next of node's previous node
            node.prev.next = node

