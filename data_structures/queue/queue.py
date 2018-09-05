#!/usr/bin/env python3


class FullQueueError(Exception):
    def __init__(self):
        super().__init__("Queue is full.")


class EmptyQueueError(Exception):
    def __init__(self):
        super().__init__("Queue is empty.")


class Queue:
    """Queue is a linear structure which follows a particular order (FIFO)."""

    def __init__(self, capacity):
        self.capacity = capacity
        self.front = 0  # Firts item from queue
        self.rear = self.capacity - 1  # Last item from queue
        self.size = 0
        self.queue = [None] * capacity

    def is_full(self):
        """Check if Queue is full (reach max of capacity)."""
        return self.size == self.capacity

    def is_empty(self):
        """Check if Queue is empty."""
        return self.size == 0

    def enqueue(self, item):
        """Add an item to queue."""
        if self.is_full():  # Check if queue is full before enqueue.
            raise FullQueueError

        # check the rear, add 1 and get module over capacity
        self.rear = (self.rear + 1) % (self.capacity)
        self.queue[self.rear] = item  # Enqueue item.
        self.size = self.size + 1  # Update size.

    def dequeue(self):
        """Remove and item from queue."""
        if self.is_empty():
            raise EmptyQueueError

        dequeued = self.queue[self.front]  # Get front from queue (FIFO)
        self.front = (self.front + 1) % (self.capacity)  # Update front
        self.size = self.size - 1

        return dequeued

    @property
    def queue_front(self):
        """Retrieve the front item from queue."""
        if self.is_empty():
            raise EmptyQueueError

        return self.queue[self.front]

    @property
    def queue_rear(self):
        """Retrieve the rear item from queue."""
        if self.is_empty():
            raise EmptyQueueError

        return self.queue[self.rear]
