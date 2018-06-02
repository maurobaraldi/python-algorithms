#!/usr/bin/env python3

from .node import Node


class SimpleLinkedList:
    """Simple Linked List implemenation."""

    def __init__(self, head=None):
        self.head = head
        self.tail = None

    def prepend(self, data):
        """Insert in first position of list."""
        self.head = Node(data, self.head)
        self.tail = self.head.next

    def append(self, data):
        """Add at the end of list."""
        if not isinstance(data, Node):
            item = Node(data)

        if self.head is None:
            self.head = item
        else:
            self.tail.next = item

        self.tail = item

        return

    def length(self):
        """Return the number of list items."""
        count = 0
        current = self.head

        while current is not None:
            count += 1
            current = current.next

        return count

    def pop(self):
        """
        Remove last item from list.

        O(n) solution.
        """
        if self.head is None:
            return None
        else:
            current = self.head
            last = None

            while current.next is not None:
                last = current
                current = current.next

            self.tail = Node(last.data)

        return current.data

    def index(self, data):
        """
        Return index position of data in list.

        If list has more than one occurance, first is returned.
        """
        index = 0
        cursor = self.head

        while cursor is not None:

            if cursor.data == data:
                return index
            else:
                cursor = cursor.next
                index += 1
