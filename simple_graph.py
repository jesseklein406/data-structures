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
            raise IndexError("Node not in graph")

        return item.edges


if __name__ == '__main__':
    from timeit import Timer

    def node_list_maker():
        node_list = []
        for i in range(101):
            new_node = Node(str(i), i)
            node_list.append(new_node)

        return node_list

    node_list = node_list_maker()

    def wide_graph():
        """
                  1
               /  |  \
            2     3   4
           /|    /|   |\
          5 6   7 8   9 1O
         /| |\ /| |\ /| |\
        11................22
        """

        wide_graph = G()

        wide_graph.add_edge(node_list[1], node_list[2])
        wide_graph.add_edge(node_list[1], node_list[3])
        wide_graph.add_edge(node_list[1], node_list[4])
        wide_graph.add_edge(node_list[2], node_list[5])
        wide_graph.add_edge(node_list[2], node_list[6])
        wide_graph.add_edge(node_list[3], node_list[7])
        wide_graph.add_edge(node_list[3], node_list[8])
        wide_graph.add_edge(node_list[4], node_list[9])
        wide_graph.add_edge(node_list[4], node_list[10])
        wide_graph.add_edge(node_list[5], node_list[11])
        wide_graph.add_edge(node_list[5], node_list[12])
        wide_graph.add_edge(node_list[6], node_list[13])
        wide_graph.add_edge(node_list[6], node_list[14])
        wide_graph.add_edge(node_list[7], node_list[15])
        wide_graph.add_edge(node_list[7], node_list[16])
        wide_graph.add_edge(node_list[8], node_list[17])
        wide_graph.add_edge(node_list[8], node_list[18])
        wide_graph.add_edge(node_list[9], node_list[19])
        wide_graph.add_edge(node_list[9], node_list[20])
        wide_graph.add_edge(node_list[10], node_list[21])
        wide_graph.add_edge(node_list[10], node_list[22])

        return wide_graph

    def long_graph():
        """
           1
           |
           2
          /|
         3 4
          /|
         5 6
          /|
         7 8
          /|
         9 10
          /|
        11 12
          /|
        13 14
          /|
        15 16
          /|
        17 18
        """

        long_graph = G()

        long_graph.add_edge(node_list[1], node_list[2])
        long_graph.add_edge(node_list[2], node_list[3])
        long_graph.add_edge(node_list[2], node_list[4])
        long_graph.add_edge(node_list[4], node_list[5])
        long_graph.add_edge(node_list[4], node_list[6])
        long_graph.add_edge(node_list[6], node_list[7])
        long_graph.add_edge(node_list[6], node_list[8])
        long_graph.add_edge(node_list[8], node_list[8])
        long_graph.add_edge(node_list[8], node_list[10])
        long_graph.add_edge(node_list[10], node_list[11])
        long_graph.add_edge(node_list[10], node_list[12])
        long_graph.add_edge(node_list[12], node_list[13])
        long_graph.add_edge(node_list[12], node_list[14])
        long_graph.add_edge(node_list[14], node_list[15])
        long_graph.add_edge(node_list[14], node_list[16])
        long_graph.add_edge(node_list[16], node_list[17])
        long_graph.add_edge(node_list[16], node_list[18])

        return long_graph

    print "\nTime for dft of wide_graph"
    print Timer(
        'wide_graph().depth_first_traversal(node_list[1])',
        'from __main__ import G, wide_graph, node_list'
    ).timeit(10) / 10

    print "\nTime for dft of long_graph"
    print Timer(
        'long_graph().depth_first_traversal(node_list[1])',
        'from __main__ import G, long_graph, node_list'
    ).timeit(10) / 10

    print "\nTime for bft of wide_graph"
    print Timer(
        'wide_graph().breadth_first_traversal(node_list[1])',
        'from __main__ import G, wide_graph, node_list'
    ).timeit(10) / 10

    print "\nTime for bft of long_graph"
    print Timer(
        'long_graph().breadth_first_traversal(node_list[1])',
        'from __main__ import G, long_graph, node_list'
    ).timeit(10) / 10

    print "\nThe dft seems to perform about three times faster than the bft"
    print "for both wide or deep graph. In general the wide and deep graphs"
    print "behave similarly relative to their size."
