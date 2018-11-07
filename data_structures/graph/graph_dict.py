#!/usr/bin/env python
from collections import defaultdict


class Graph:
    """Direct graph representation using adjacency list."""

    def __init__(self, vertices=1):
        self.vertices =  vertices
        self.graph = defaultdict(list)  # Store graph in a dict

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, s):
        """Breadth First Search graph."""
        visited = [False] * len(self.graph)  # Mark all the vertices as not visietd
        
        queue = []
        queue.append(s)  # Enqueue node s

        visited[s] = True  # Mark it as visited

        while queue:
            s = queue.pop(0)  # Dequeue a vertex from queue and print it
            print(s, end=" ")

            for i in self.graph[s]:  # get all dajcent vertices of the dequeued vertex s.
                if visited[i] == False:  # If adjacent has not been visited
                    queue.append(i)      # enqueue it
                    visited[i] = True    # mark it as visited

    def __dfs(self, v, visited):

        visited[v] = True  # Mark the current node as visited
        print(v,)

        for i in self.graph[v]:  # Recur for all the vertices adjacent tho this vertex
            if visited[i] == False:
                self.__dfs(i, visited)

    def dfs(self, v=None):
        """Depth First Search grpah."""

        if v is not None:
            visited = [False] * len(self.graph)
            self.__dfs(v, visited)

        else:  # Traverse graph from all vertices one by one
            v = len(self.graph)
            visited = [False] * v

            for i in range(v): 
                if visited[i] == False:
                    self.__dfs(i, visited)

    def mother(self):
        """Returns vertex's mother if exists, otherwise -1."""
        
        visited = [False] * self.vertices
        v = 0  # To store last visited finished vertex (or mother)

        for i in range(self.vertices):  # Do DFS traversal and find the last finished
            if visited[i] == False:
                self.__dfs(i, visited)
                v = i

        # Reset all values in visited[] as false and do
        # DFS beginning from v to check if all vertices are
        # reachable from it or not.
        visited = [False] * self.vertices
        self.__dfs(v, visited)

        if any(i == False for i in visited):
            return -1
        else:
            return v
