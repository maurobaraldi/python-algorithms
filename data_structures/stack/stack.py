#!/usr/bin/env python3


class EmptyStackError(Exception):
    """Exception for operations when stack is empty."""
    def __init__(self):
        super().__init__("Stack is empty.")


class FullStackError(Exception):
    """Exception for operations when stack is full."""
    def __init__(self):
        super().__init__("Stack is full.")


class Stack:
    """Stack data structure using Lists as a base structure."""
    def __init__(self, max_size=1):
        self.max_size = max_size
        self.stack = []

    def is_empty(self):
        """Check is Stack is empty."""
        return self.size() == 0

    def is_full(self):
        """Check if stack is full."""
        return self.size() == self.max_size

    def push(self, item):
        """Add an element, at the top, of Stack"""
        if self.is_full():
            raise FullStackError

        self.stack.append(item)

    def pop(self):
        """Remove an element, last pushed, of Stack"""
        if self.is_empty():
            raise EmptyStackError

        return self.stack.pop()

    def peek(self):
        """Return top element of the Stac."""
        if self.is_empty():
            raise EmptyStackError

        return self.stack[len(self.stack) - 1]

    def size(self):
        return len(self.stack)

