#!/usr/bin/env python


class Node:
    def __init__(self, data):
        self.vertex = data
        self.next = None


class Graph:
    """Adjacency list representation by a Graph."""
    def __init__(self, vertices):
        self.v = vertices
        self.graph = [None] * self.v

    def add_edge(self, src, dest):
        """Add and edge to undirected graph."""
        node = Node(dest)  # Adding node to the source node
        node.next = self.graph[src]
        self.graph[src] = node

        node = Node(src)  # Adding source node to the destination
        node.next = self.graph[dest]
        self.graph[dest] = node

    def print(self):

        for i in range(self.v):
            print("Adjacency list of vertex{}\n head.".format(i), end="")
            temp = self.graph[i]

            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next

            print(" \n")

