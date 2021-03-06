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
    # jerry2allen = simple_graph.Edge(jerry, allen)
    # allen2six = simple_graph.Edge(allen, six)
    create_graph.add_node(jerry)
    create_graph.add_node(allen)
    create_graph.add_node(six)
    create_graph.add_edge(jerry, allen)
    create_graph.add_edge(allen, six)
    return create_graph


# g.nodes(): return a list of all nodes in the graph
def test_nodes(build_graph):
    build_graph_node_names = [i.name for i in build_graph.nodes()]
    assert set(build_graph_node_names) == set(['Jerry', 'Allen', '6'])


# g.edges(): return a list of all edges in the graph
def test_edges(build_graph):
    build_graph_edge_names = [(i[0].name, i[1].name) for i in build_graph.edges()]
    assert set(build_graph_edge_names) == set([('Jerry', 'Allen'), ('Allen', '6')])


# g.add_node(n): adds a new node 'n' to the graph
def test_add_node(build_graph):
    new_node = simple_graph.Node('Jimmy', 0)
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


def test_add_edge_from_new_nodes():
    new_node1 = simple_graph.Node('new1', 1)
    new_node2 = simple_graph.Node('new2', 2)
    build_graph.add_edge(new_node1, new_node2)
    assert new_node1, new_node2 in build_graph.edges()


# g.del_node(n): deletes the node 'n' from the graph, raises an error if no
# such node exists
def test_del_node(build_graph):
    current_node = build_graph.nodes()[0]
    build_graph.del_node(current_node)
    assert current_node not in build_graph.nodes()
    
    # we expect edges to be consistent and updated with nodes
    assert current_node not in [
        build_graph.edges()[i] for i in range(len(build_graph.edge()))
    ]


def test_del_nonexistent_node(build_graph):
    new_node = simple_graph.Node('new', 1)
    # not in build_graph
    with pytest.raises(ValueError):
        assert build_graph.del_node(new_node)


# g.del_edge(n1, n2): deletes the edge connecting 'n1' and 'n2' from the graph,
# raises an error if no such edge exists
def test_del_edge(build_graph):
    current_edge = build_graph.edges()[0]
    build_graph.del_edge(current_edge)
    assert current_edge not in build_graph.edges()


def test_del_nonexistent_edge(build_graph):
    new_node1 = simple_graph.Node('new1', 1)
    new_node2 = simple_graph.Node('new2', 2)
    new_edge = (new_node1, new_node2)
    with pytest.raises(ValueError):
        assert build_graph.del_node(new_edge)


# g.has_node(n): True if node 'n' is contained in the graph, False if not.
def test_has_node(build_graph):
    contained_node = build_graph.nodes()[0]
    assert build_graph.test_has_node(contained_node)


def test_node_not_contained(build_graph):
    new_node = simple_graph.Node('new', 1)
    assert not build_graph.test_has_node(new_node)


# g.neighbors(n): returns the list of all nodes connected to 'n' by edges,
# raises an error if n is not in g
def test_neighbors(build_graph):
    pass


# g.adjacent(n1, n2): returns True if there is an edge connecting n1 and n2,
# False if not, raises an error if either of the supplied nodes are not in g
def test_adjacent(build_graph):
    pass
