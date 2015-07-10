#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import pytest
import simple_graph


@pytest.fixture(scope="function")
def create_graph():
    new_graph = simple_graph.G()
    return new_graph


@pytest.fixture(scope="function")
def build_graph(create_graph):
    jerry = simple_graph.Node('Jerry', 5)
    allen = simple_graph.Node('Allen', 8)
    six = simple_graph.Node('6', 6)
    create_graph.add_node(jerry)
    create_graph.add_node(allen)
    create_graph.add_node(six)
    create_graph.add_edge(jerry, allen)
    create_graph.add_edge(allen, six)
    return create_graph


# g.nodes(): return a list of all nodes in the graph
def test_nodes(build_graph):
    build_graph_names = [i.name for i in build_graph.nodes()]
    assert set(build_graph_names) == set(['Jerry', 'Allen', '6'])


# g.edges(): return a list of all edges in the graph
def test_edges(build_graph):
    build_graph_edges = [(i.name, y.name) for i, y in build_graph.edges()]
    assert set(build_graph_edges) == set([('Jerry', 'Allen'), ('Allen', '6')])


# g.add_node(n): adds a new node 'n' to the graph
def test_add_node(build_graph):
    new_node = simple_graph.Node('new', 1)
    build_graph.add_node(new_node)
    assert new_node in build_graph.nodes()


# g.add_edge(n1, n2): adds a new edge to the graph connecting 'n1' and 'n2', if
# either n1 or n2 are not already present in the graph, they should be added.
def test_add_edge(build_graph):
    new_node1 = simple_graph.Node('new1', 1)
    new_node2 = simple_graph.Node('new2', 2)
    build_graph.add_node(new_node1)
    build_graph.add_node(new_node2)
    build_graph.add_edge(new_node1, new_node2)
    assert new_node1, new_node2 in build_graph.edges()


def test_add_edge_and_nodes(build_graph):
    new_node1 = simple_graph.Node('new1', 1)
    new_node2 = simple_graph.Node('new2', 2)
    build_graph.add_edge(new_node1, new_node2)
    assert new_node1, new_node2 in build_graph.edges()
    assert new_node1 in build_graph.nodes() and new_node2 in build_graph.nodes()


# g.del_node(n): deletes the node 'n' from the graph, raises an error if no
# such node exists
def test_del_node(build_graph):
    current_node = build_graph.nodes()[0]
    build_graph.del_node(current_node)
    assert current_node not in build_graph.nodes()

    # check that its edges are removed as well
    for edge in build_graph.edges():
        assert current_node not in edge


def test_del_node_nonexistent(build_graph):
    new_node = simple_graph.Node('new', 1)
    with pytest.raises(KeyError):
        build_graph.del_node(new_node)


# g.del_edge(n1, n2): deletes the edge connecting 'n1' and 'n2' from the graph,
# raises an error if no such edge exists
def test_del_edge(build_graph):
    current_edge = build_graph.edges()[0]
    build_graph.del_edge(*current_edge)
    assert current_edge not in build_graph.edges()

    # try to delete, check for error
    with pytest.raises(KeyError):
        build_graph.del_edge(*current_edge)


# g.has_node(n): True if node 'n' is contained in the graph, False if not.
def test_has_node(build_graph):
    current_node = build_graph.nodes()[0]
    assert build_graph.has_node(current_node)


def test_has_no_node(build_graph):
    new_node = simple_graph.Node('new', 1)
    assert not build_graph.has_node(new_node)


# g.neighbors(n): returns the list of all nodes connected to 'n' by edges,
# raises an error if n is not in g
def test_neighbors(build_graph):
    current_node = build_graph.nodes()[0]
    neighbors = set()
    for edge in build_graph.edges():
        if edge[0] is current_node:
            neighbors.add(edge[1])

    assert build_graph.neighbors(current_node) == list(neighbors)


def test_neighbors_nonexistent(build_graph):
    new_node = simple_graph.Node('new', 1)
    with pytest.raises(ValueError):
        build_graph.neighbors(new_node)


# g.adjacent(n1, n2): returns True if there is an edge connecting n1 and n2,
# False if not, raises an error if either of the supplied nodes are not in g
def test_adjacent(build_graph):
    current_node1 = build_graph.nodes()[0]
    current_node2 = build_graph.neighbors(current_node1)[0]   # pull a neighbor
    assert build_graph.adjacent(current_node1, current_node2)

    new_node = simple_graph.Node('new', 1)
    build_graph.add_node(new_node)
    assert not build_graph.adjacent(current_node1, new_node)


def test_adjacent_nonexistent(build_graph):
    current_node = build_graph.nodes()[0]
    new_node = simple_graph.Node('new', 1)
    with pytest.raises(ValueError):
        build_graph.adjacent(current_node, new_node)
