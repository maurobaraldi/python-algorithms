#!/usr/bin/env python


class Node:
    def __init__(self, data=None):
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
        """
        Insert a new node at the beginning of Linked List.

        Time Complexity: O(1), We have a pointer to the head and we can
        directly attach a node and change the pointer. So the Time complexity
        of inserting a node at the head position is O(1) as it does a constant
        amount of work.
        Auxiliary Space: O(1)
        """

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

        while last.next:  # Traverse all the LL until last node
            last = last.next

        last.next = node  # Then, set last node as appended node

    def delete(self, data):
        """
        Delete the firts node found matching th data.

        Best Case: O(1) if given position is 1
        Average  & Worst Case: O(N) where N is the length of the linked list.
        This is because in the worst case, we need to traverse the entire
        linked list to find the node to be deleted.
        """

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

    def exists(self, data):
        """
        Traverse across the Linked list to check if data exists.

        Time Complexity: O(N), Where N is the number of nodes in the LinkedList
        Auxiliary Space: O(1)
        """

        current = self.head

        while current is not None:
            if current.data == data:
                return True
            else:
                current = current.next

    def exists_recursive(self, _list, data):
        """
        Traverse across the Linked list to check if data exists (recursively).

        Time Complexity: O(N)
        Auxiliary Space: O(N), Stack space used by recursive calls
        """

        if not _list: # Base case
            return False

        if _list.data == data: # If data found in current node, return true
            return True

        return self.exists_recursive(_list.next, data) # Recur for remaining list
    
    def get_node(self, index):
        """
        Get the Nth node of linked list.

        Time Complexity: O(n)
        Auxiliary Space: O(1) space created for variables
        """

        current = self.head
        count = 0

        while current: # Loop while end of linked list is not reached
            if count == index:
                return current.data
            count += 1
            current = current.next
        
        return 0

    @property
    def length(self):
        """
        Get the length of a linked list (interactively).

        Time complexity: O(N), Where N is the size of the linked list
        Auxiliary Space: O(1), As constant extra space is used.
        """

        current = self.head
        length = 0

        while current is not None:
            length += 1
            current = current.next

        return length

    def length_recursive(self, node):
        """
        Get the length of a linked list (interactively).

        Time complexity: O(N), Where N is the size of the linked list
        Auxiliary Space: O(1), As constant extra space is used.
        """

        if node is not None:
            return 1 + self.length_recursive(node.next)
        else:
            return 0

    def reverse(self):
        """
        Reverese the Linked List.

        Time Complexity: O(N), Traversing over the linked list of size N.
        Auxiliary Space: O(1)
        """
        previous = None
        current = self.head

        while current is not None:
            next = current.next
            current.next = previous
            previous = current
            current = next

        self.head = previous

    def reverse_recursive(self, head):
        """
        Reverese the Linked List (recursively).

        Time Complexity: O(N), Traversing over the linked list of size N.
        Auxiliary Space: O(1)
        """

        if head is None or head.next is None: # If head is empty or has reached the list end
            return head

        tail = self.reverse_recursive(head.next)

        head.next.next = head # Put first element at the end
        head.next = None

        return tail
