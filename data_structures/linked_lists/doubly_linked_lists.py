#!/usr/bin/env python3


class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data  # Assign to node data
        self.next = next  # Assign to node next node
        self.prev = prev  # Assign to node previous node


class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Initialize Doubly Linked List object
        self.tail = None

    def push(self, data):
        """Insert a new node at the beginning of DLL."""
        node = Node(data)  # Allocate the Node and put it the data
        node.next = self.head  # Make the head, as the next of node

        if self.head is not None:  # Change prev of head node to new_node
            self.head.prev = node

        self.head = node  # Move the head to point to the new node

    def append(self, data):
        """Append a new node at the end of Doubly Linked List."""
        node = Node(data)

        if self.head is None:  # If DLL is empty, the new node is head.
            self.head = self.tail = node
        else:
            node.prev = self.tail
            node.next = None
            self.tail.next = node
            self.tail = node

    def remove(self, node_data):
        """Remove a node from Doubly Linked List."""
        current = self.head  # Set cursor to head

        while current is not None:  # Traverse whole DLL
            if current.data == node_data:  # Found node
                if current.prev is not None:  # If it's not the first element
                    current.prev.next = current.next
                    current.next.prev = current.prev
                else:
                    self.head = current.next
                    current.next.prev = None

            current = current.next
