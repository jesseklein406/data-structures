#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test for graph traversal"""

from __future__ import unicode_literals
import simple_graph as gt
import pytest


@pytest.fixture(scope="function")
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


@pytest.fixture(scope="function")
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

def test_dft_on_wide_at_root(node_list, wide_graph, wide_graph_map):
    start = node_list[1]
    actualdwr = wide_graph.depth_first_traversal(start)

    for node in enumerate(actualdwr):
        for item in wide_graph_map.iteritems():
            if node[1] in item[1]:
                actualdwr[node[0]] = item[0]

    expected = [
        1, 2, 3, 4, 4, 3, 4, 4, 2, 3, 4,
        4, 3, 4, 4, 2, 3, 4, 4, 3, 4, 4
    ]

    assert expected == actualdwr


def test_dft_on_wide_at_middle(node_list, wide_graph, wide_graph_map):
    start = node_list[2]
    actualdwm = wide_graph.depth_first_traversal(start)

    for node in enumerate(actualdwm):
        for item in wide_graph_map.iteritems():
            if node[1] in item[1]:
                actualdwm[node[0]] = item[0]

    expected = [2, 3, 4, 4, 3, 4, 4]

    assert expected == actualdwm


def test_dft_on_long_at_root(node_list, long_graph):
    start = node_list[1]
    actualdlr = long_graph.depth_first_traversal(start)

    actual_values = [i.value for i in actualdlr]

    traverse_up = []
    end = actual_values.pop()
    while end != 18:
        traverse_up.append(end)
        end = actual_values.pop()

    assert actual_values == sorted(actual_values)
    assert traverse_up == sorted(traverse_up)


def test_dft_on_long_at_middle(node_list, long_graph):
    start = node_list[8]
    actualdlm = long_graph.depth_first_traversal(start)

    actual_values = [i.value for i in actualdlm]

    traverse_up = []
    end = actual_values.pop()
    while end != 18:
        traverse_up.append(end)
        end = actual_values.pop()

    assert actual_values == sorted(actual_values)
    assert traverse_up == sorted(traverse_up)


def test_dft_on_cyclic(node_list, cyclic_graph):
    start = node_list[1]
    actualdc = cyclic_graph.depth_first_traversal(start)

    actual_values = [i.value for i in actualdc]

    assert actual_values == range(1, 11)


# g.breadth_first_traversal(start): Perform a full breadth-first traversal of
# the graph, beginning at start. Return the full visited path when traversal is
# complete.

def test_bft_on_wide_at_root(node_list, wide_graph, wide_graph_map):
    start = node_list[1]
    actualbwr = wide_graph.breadth_first_traversal(start)

    for node in enumerate(actualbwr):
        for item in wide_graph_map.iteritems():
            if node[1] in item[1]:
                actualbwr[node[0]] = item[0]

    expected = [
        1, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4,
        4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4
    ]

    assert expected == actualbwr


def test_bft_on_wide_at_middle(node_list, wide_graph, wide_graph_map):
    start = node_list[2]
    actualbwm = wide_graph.breadth_first_traversal(start)

    for node in enumerate(actualbwm):
        for item in wide_graph_map.iteritems():
            if node[1] in item[1]:
                actualbwm[node[0]] = item[0]

    expected = [2, 3, 3, 4, 4, 4, 4]

    assert expected == actualbwm


def test_bft_on_long_at_root(node_list, long_graph):
    start = node_list[1]
    actualblr = long_graph.breadth_first_traversal(start)

    actual_values = [i.value for i in actualblr]

    odds = []
    evens = []
    while actual_values:
        odds.append(actual_values.pop(0))
        if actual_values:
            evens.append(actual_values.pop(0))

    assert odds == sorted(odds)
    assert evens == sorted(evens)


def test_bft_on_long_at_middle(node_list, long_graph):
    start = node_list[8]
    actualblm = long_graph.breadth_first_traversal(start)

    actual_values = [i.value for i in actualblm]

    odds = []
    evens = []
    while actual_values:
        odds.append(actual_values.pop(0))
        if actual_values:
            evens.append(actual_values.pop(0))

    assert odds == sorted(odds)
    assert evens == sorted(evens)


def test_bft_on_cyclic(node_list, cyclic_graph):
    start = node_list[1]
    actualbc = cyclic_graph.breadth_first_traversal(start)

    actual_values = [i.value for i in actualbc]

    assert actual_values == range(1, 11)
