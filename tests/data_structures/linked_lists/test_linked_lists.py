#!/usr/bin/env python

import unittest
from data_structures.linked_lists.linked_lists import Node, LinkedList
from data_structures.linked_lists.problems import *


class TestNode(unittest.TestCase):

   def test_define_a_node(self):
        node = Node(1)

        self.assertIsInstance(node, Node)
        self.assertEqual(node.data, 1)


class TestLinkdeList(unittest.TestCase):

    def test_instantiate_a_linked_list(self):
        linkedl = LinkedList()
        linkedl.head = Node(1)

        self.assertIsInstance(linkedl, LinkedList)
        self.assertEqual(linkedl.head.data, 1)

    def test_instantiate_a_linked_list_with_three_nodes(self):
        linkedl = LinkedList()

        first = Node(1)
        second = Node(2)
        third = Node(3)

        linkedl.head = first
        linkedl.head.next = second

        second.next = third

        self.assertEqual(linkedl.head.data, 1)
        self.assertEqual(linkedl.head.next.data, 2)
        self.assertEqual(linkedl.head.next.next.data, 3)

    def test_push_node_to_linked_list(self):
        linked_list = LinkedList()

        linked_list.head = Node(1)
        linked_list.push(2)

        self.assertEqual(linked_list.head.data, 2)
        self.assertEqual(linked_list.head.next.data, 1)

    def test_insert_after_node_in_linked_list(self):
        linked_list = LinkedList()

        linked_list.head = Node(1)
        linked_list.head.next = Node(2)
        linked_list.insert_after(linked_list.head, 3)
        linked_list._print()

        self.assertEqual(linked_list.head.data, 1)
        self.assertEqual(linked_list.head.next.data, 3)
        self.assertEqual(linked_list.head.next.next.data, 2)

    def test_append_node_to_linked_list(self):
        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(3)
        linked_list.append(6)

        self.assertEqual(linked_list.head.data, 1)
        self.assertEqual(linked_list.head.next.data, 3)
        self.assertEqual(linked_list.head.next.next.data, 6)

    def test_delete_node_from_linked_list(self):
        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)
        linked_list.delete(2)

        self.assertEqual(linked_list.head.data, 1)
        self.assertEqual(linked_list.head.next.data, 3)
 
    def test_reverse_a_linked_list_interactively(self):
        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)
        linked_list.reverse()

        self.assertEqual(linked_list.head.data, 3)
        self.assertEqual(linked_list.head.next.next.data, 1)

    @unittest.skip("Testing")
    def test_reverse_a_linked_list_recursively(self):
        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)
        linked_list.reverse_recursive(linked_list.head)

        self.assertEqual(linked_list.head.data, 3)
        self.assertEqual(linked_list.head.next.next.data, 1)

    def test_search_element_in_linked_list_interactively(self):
        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)
        self.assertTrue(linked_list.exists(2))
        self.assertFalse(linked_list.exists(4))

    def test_search_element_in_linked_list_recursively(self):
        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)
        self.assertTrue(linked_list.exists_recursive(linked_list.head, 2))
        self.assertFalse(linked_list.exists_recursive(linked_list.head, 4))

    def test_search_element_by_index_in_linked_list(self):
        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)
        self.assertTrue(linked_list.get_node(1), 2)
        self.assertFalse(linked_list.get_node(4), 0)

    def test_get_length_of_a_linked_list_interactively(self):
        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)
        self.assertEqual(linked_list.length, 3)
 
    def test_get_length_of_a_linked_list_recursively(self):
        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)
        self.assertEqual(linked_list.length_recursive(linked_list.head), 3)

    ## Problems solved with Linked Lists - LeetCode
        
    def test_leetcode_merge_two_sorted_lists(self):
        L1 = ListNode(val=1)
        L1.next = ListNode(val=2)
        L1.next.next = ListNode(val=4)
        L2 = ListNode(val=1)
        L2.next = ListNode(val=3)
        L2.next.next = ListNode(val=4)
        res = SolutionLeetCode1().mergeTwoLists(L1, L2)

        self.assertTrue(
            all([
                res.val == 1, 
                res.next.val == 1, 
                res.next.next.val == 2, 
                res.next.next.next.val == 3,
                res.next.next.next.next.val == 4
            ])
        )

        
    ## Problems with Linked Lists - Geeks for Geeks
        
    def test_find_middle_in_a_odd_elements_linked_list(self):
        """
        Time Complexity: O(n), for traversing.
        Auxiliary Space: O(n), for Vector.
        """

        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)
        linked_list.append(4)
        linked_list.append(5)

        current = linked_list.head
        values = []

        while current is not None:
            values.append(current.data)
            current = current.next
        
        self.assertEqual(values[len(values)//2], 3)
    
    def test_count_occurences_of_element_in_a_linked_list(self):
        """
        Time Complexity: O(n) 
        Auxiliary Space: O(1)
        """

        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)
        linked_list.append(4)
        linked_list.append(5)
        linked_list.append(2)

        value = 2
        current = linked_list.head
        counter = 0

        while current is not None:
            if current.data == value:
                counter += 1
            current = current.next
        
        self.assertEqual(counter, 2)
