#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test for graph traversal"""'''

from __future__ import unicode_literals
import graph_traversal as gt
import pytest


@pytest.fixture(scope="module")
def node_list():
    node_list = []
    for i in range(101):
        new_node = gt.Node(str(i), i)
        node_list.append(new_node)

    return node_list


@pytest.fixture(scope="function")
def wide_graph(node_list):
    """
              1
           /  |  \
        2     3   4
       /|    /|   |\
      5 6   7 8   9 1O
     /| |\ /| |\ /| |\
    11................22
    """

    wide_graph = gt.G()

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


@pytest.fixture(scope="module")
def wide_graph_map(node_list):
    wide_graph_map = {
        1: [node_list[1]],
        2: [node_list[2], node_list[3], node_list[4]],
        3: [node_list[i] for i in range(5, 11)],
        4: [node_list[i] for i in range(11, 23)]
    }

    return wide_graph_map


@pytest.fixture(scope="function")
def long_graph(node_list):
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

    long_graph = gt.G()

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


@pytest.fixture(scope="function")
def huge_graph(node_list):
    """
    1  -  2 -  3 -  4 -  5 -  6 -  7 -  8 -  9 - 10
    |
    11 - 12 - 13 - 14 - 15 - 16 - 17 - 18 - 19 - 20
    |
    21 - 22 - 23 - 24 - 25 - 26 - 27 - 28 - 29 - 30
    |
    31 - 32 - 33 - 34 - 35 - 36 - 37 - 38 - 39 - 40
    |
    41 - 42 - 43 - 44 - 45 - 46 - 47 - 48 - 49 - 50
    |
    51 - 52 - 53 - 54 - 55 - 56 - 57 - 58 - 59 - 60
    |
    61 - 62 - 63 - 64 - 65 - 66 - 67 - 68 - 69 - 70
    |
    71 - 72 - 73 - 74 - 75 - 76 - 77 - 78 - 79 - 80
    |
    81 - 82 - 83 - 84 - 85 - 86 - 87 - 88 - 89 - 90
    |
    91 - 92 - 93 - 94 - 95 - 96 - 97 - 98 - 99 - 100
    """

    huge_graph = gt.G()

    for i in range(9):
        i = 10 * i + 1
        huge_graph.add_edge(node_list[i], node_list[i + 10])

    for i in range(10):
        i = 10 * i
        for j in range(1, 10):
            huge_graph.add_edge(node_list[i + j], node_list[i + j + 1])

    return huge_graph


@pytest.fixture(scope="function")
def small_graph(node_list):
    """
        1
       / \
      2   3
     / \   \
    4   5   6
    """

    small_graph = gt.G()

    small_graph.add_edge(node_list[1], node_list[2])
    small_graph.add_edge(node_list[1], node_list[3])
    small_graph.add_edge(node_list[2], node_list[4])
    small_graph.add_edge(node_list[2], node_list[5])
    small_graph.add_edge(node_list[3], node_list[6])

    return small_graph


@pytest.fixture(scope="function")
def cyclic_graph(node_list):
    """
    1  -  2 -  3 -  4
    |               |
    10              5
    |               |
    9  -  8 -  7 -  6
    """

    cyclic_graph = gt.G()

    for i in range(1, 10):
        cyclic_graph.add_edge(node_list[i], node_list[i + 1])

    cyclic_graph.add_edge(node_list[10], node_list[1])

    return cyclic_graph


# g.depth_first_traversal(start): Perform a full depth-first traversal of the
# graph beginning at start. Return the full visited path when traversal is
# complete.

def test_dft_on_wide_at_root(wide_graph, node_list, wide_graph_map):
    start = node_list[1]
    actual = wide_graph.depth_first_traversal(start)

    for node in enumerate(actual):
        for item in wide_graph_map.iteritems():
            if node[1] in item[1]:
                actual[node[0]] = item[0]

    expected = [
        1, 2, 3, 4, 4, 3, 4, 4, 2, 3, 4,
        4, 3, 4, 4, 2, 3, 4, 4, 3, 4, 4
    ]

    assert expected == actual


def test_dft_on_wide_at_middle(wide_graph):
    start = node_list[2]
    actual = wide_graph.depth_first_traversal(start)

    for node in enumerate(actual):
        for item in wide_graph_map.iteritems():
            if node[1] in item[1]:
                actual[node[0]] = item[0]

    expected = [2, 3, 4, 4, 3, 4, 4]

    assert expected == actual


def test_dft_on_long_at_root(long_graph):
    start = node_list[1]
    actual = long_graph.depth_first_traversal(start)

    actual_values = [i.value for i in actual]
    


def test_dft_on_long_at_middle(long_graph):
    pass


def test_dft_on_huge_at_root(huge_graph):
    pass


def test_dft_on_huge_at_middle(huge_graph):
    pass


def test_dft_on_small(small_graph):
    pass


def test_dft_on_cyclic(cyclic_graph):
    pass


# g.breadth_first_traversal(start): Perform a full breadth-first traversal of
# the graph, beginning at start. Return the full visited path when traversal is
# complete.

def test_bft_on_wide_at_root(wide_graph):
    pass


def test_bft_on_wide_at_middle(wide_graph):
    pass


def test_bft_on_long_at_root(long_graph):
    pass


def test_bft_on_long_at_middle(long_graph):
    pass


def test_bft_on_huge_at_root(huge_graph):
    pass


def test_bft_on_huge_at_middle(huge_graph):
    pass


def test_bft_on_small(small_graph):
    pass


def test_bft_on_cyclic(cyclic_graph):
    pass'''
