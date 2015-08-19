#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test for weighted edges"""

from __future__ import unicode_literals
import pytest
import simple_graph as g


@pytest.fixture(scope="function")
def node_list():
    node_list = []
    for i in range(101):
        new_node = g.Node(str(i), i)
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

    wide_graph = g.G()

    wide_graph.add_edge(node_list[1], node_list[2], 5)
    wide_graph.add_edge(node_list[1], node_list[3], 5)
    wide_graph.add_edge(node_list[1], node_list[4], 5)
    wide_graph.add_edge(node_list[2], node_list[5], 5)
    wide_graph.add_edge(node_list[2], node_list[6], 5)
    wide_graph.add_edge(node_list[3], node_list[7], 5)
    wide_graph.add_edge(node_list[3], node_list[8], 5)
    wide_graph.add_edge(node_list[4], node_list[9], 5)
    wide_graph.add_edge(node_list[4], node_list[10], 5)
    wide_graph.add_edge(node_list[5], node_list[11], 5)
    wide_graph.add_edge(node_list[5], node_list[12], 5)
    wide_graph.add_edge(node_list[6], node_list[13], 5)
    wide_graph.add_edge(node_list[6], node_list[14], 5)
    wide_graph.add_edge(node_list[7], node_list[15], 5)
    wide_graph.add_edge(node_list[7], node_list[16], 5)
    wide_graph.add_edge(node_list[8], node_list[17], 5)
    wide_graph.add_edge(node_list[8], node_list[18], 5)
    wide_graph.add_edge(node_list[9], node_list[19], 5)
    wide_graph.add_edge(node_list[9], node_list[20], 5)
    wide_graph.add_edge(node_list[10], node_list[21], 5)
    wide_graph.add_edge(node_list[10], node_list[22], 5)

    return wide_graph


def test_edges_are_weighted(wide_graph):
    for v in wide_graph:
        for w in wide_graph[v]:
            assert wide_graph[v][w] == 5


def test_weight_not_integer(wide_graph):
    with pytest.raises(ValueError):
        wide_graph.add_edge(node_list[1], node_list[10], 'p')


def test_node_not_in_graph(wide_graph):
    bad_node = g.Node('bad', 'node')
    with pytest.raises(IndexError):
        print wide_graph[bad_node]


def test_delete_edge(wide_graph):
    wide_graph.del_edge(node_list[10], node_list[22])
    with pytest.raises(IndexError):
        print node_list[10].edges[node_list[22]]
