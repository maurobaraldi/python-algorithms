#!/usr/bin/env python

import unittest
from data_structures.queue.queue import Queue


class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = Queue(1)

    def test_instantiate_a_queue(self):
        self.assertIsInstance(self.queue, Queue)

    def test_queue_is_full(self):
        self.assertFalse(self.queue.is_full())

    def test_queue_is_empty(self):
        self.assertTrue(self.queue.is_empty())

    def test_enqueue_an_item(self):
        self.queue.enqueue(2)
        self.assertFalse(self.queue.is_empty())

    def test_dequeue_an_item(self):
        self.queue.enqueue(2)
        self.assertEquals(self.queue.dequeue(), 2)
        self.assertTrue(self.queue.is_empty())

    def test_get_front_from_queue(self):
        self.queue.enqueue(2)
        self.assertEquals(self.queue.queue_front, 2)

    def test_get_rear_from_queue(self):
        self.queue.enqueue(2)
        self.assertEquals(self.queue.queue_rear, 2)
