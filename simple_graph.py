#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A data structure for a simple graph using the model from Martin BroadHurst
http://www.martinbroadhurst.com/graph-data-structures.html
"""

from Queue import Queue


class Node(object):
    """A Node class for use in a simple graph"""
    def __init__(self, name, value):
        """Make a new node object"""
        self.name = name
        self.value = value
        self.edges = {}


class G(tuple):
    """A data structure for a simple graph"""
    def __init__(self):
        """Make a new simple graph object"""
        self.nodes_ = set()
        self.edges_ = set()

    def __repr__(self):
        return (self.nodes_, self.edges_)

    def nodes(self):
        """return a list of all nodes in the graph"""
        return list(self.nodes_)

    def edges(self):
        """return a list of all edges in the graph"""
        return list(self.edges_)

    def add_node(self, n):
        """adds a new node 'n' to the graph"""
        self.nodes_.add(n)

    def add_edge(self, n1, n2, weight):
        """adds a new edge to the graph connecting 'n1' and 'n2', if either n1
        or n2 are not already present in the graph, they should be added.
        """
        weight = int(weight)

        if n1 not in self.nodes_:
            self.nodes_.add(n1)

        if n2 not in self.nodes_:
            self.nodes_.add(n2)

        self.edges_.add((n1, n2))
        n1.edges[n2] = weight

    def del_node(self, n):
        """deletes the node 'n' from the graph, raises an error if no such node exists
        """
        self.nodes_.remove(n)

        for edge in self.edges_.copy():
            if n in edge:
                self.edges_.remove(edge)

    def del_edge(self, n1, n2):
        """deletes the edge connecting 'n1' and 'n2' from the graph, raises an
        error if no such edge exists
        """
        self.edges_.remove((n1, n2))
        del n1.edges[n2]

    def has_node(self, n):
        """True if node 'n' is contained in the graph, False if not.
        """
        return n in self.nodes_

    def neighbors(self, n):
        """returns the list of all nodes connected to 'n' by edges, raises an
        error if n is not in g
        """
        if n not in self.nodes_:
            raise ValueError("Node not in graph")

        neighbors = set()
        for edge in self.edges_:
            if edge[0] is n:
                neighbors.add(edge[1])

        return list(neighbors)

    def adjacent(self, n1, n2):
        """returns True if there is an edge connecting n1 and n2, False if not,
        raises an error if either of the supplied nodes are not in g
        """
        if n1 not in self.nodes_ or n2 not in self.nodes_:
            raise ValueError("Both nodes not in graph")

        for edge in self.edges_:
            if n1 in edge and n2 in edge:
                return True

        return False

    def depth_first_traversal(self, start, discovered=None):
        """Perform a full depth-first traversal of the graph beginning at
        start. Return the full visited path when traversal is complete.
        """
        if discovered is None:
            discovered = []

        discovered.append(start)
        for neighbor in self.neighbors(start):
            if neighbor not in discovered:
                self.depth_first_traversal(neighbor, discovered=discovered)
        return discovered

    def breadth_first_traversal(self, start):
        """Perform a full breadth-first traversal of the graph, beginning at
        start. Return the full visited path when traversal is complete.
        """
        result = []
        q = Queue()

        q.put(start)

        while not q.empty():
            n = q.get()
            result.append(n)
            for neighbor in self.neighbors(n):
                if neighbor not in result:
                    q.put(neighbor)

        return result

    def __getitem__(self, item):
        if item not in self.nodes_:
            raise KeyError("Node not in graph")

        return item.edges
