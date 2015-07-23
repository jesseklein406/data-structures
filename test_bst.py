#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pytest
import bst


@pytest.fixture(scope="function")
def initial_node():
    initial_node = bst.Node(10)
    return initial_node


@pytest.fixture(scope="function")
def built_tree():
    tree_root = bst.Node(10)
    vals = [5, 15, 3, 7, 12, 20, 2, 4, 6, 9, 11, 14, 18, 22]
    for val in vals:
        tree_root.insert(val)
    return tree_root


def test_add_same_node(initial_node):
    initial_node.insert(10)
    assert initial_node.left is None
    assert initial_node.right is None


def test_add_new_node(initial_node):
    initial_node.insert(11)
    assert initial_node.left is None
    assert initial_node.right.value == 11


def test_size(initial_node):
    assert initial_node.size() == 1
    initial_node.insert(11)
    assert initial_node.size() == 2


def test_contains(initial_node):
    assert initial_node.contains(11) is False
    initial_node.insert(11)
    assert initial_node.contains(11) is True


def test_depth(initial_node):
    assert initial_node.depth() == 1
    initial_node.insert(11)
    assert initial_node.depth() == 2


def test_balance(initial_node):
    assert initial_node.balance() == 0
    initial_node.insert(11)
    assert initial_node.balance() == -1


def test_built_size(built_tree):
    assert built_tree.size() == 15


def test_built_depth(built_tree):
    assert built_tree.depth() == 4


def test_built_balance(built_tree):
    assert built_tree.balance() == 0


def test_add_to_built_tree(built_tree):
    built_tree.insert(13)
    assert built_tree.depth() == 5
    assert built_tree.balance() == -1


@pytest.fixture(scope="function")
def built_tree_no_branches(initial_node):
    no_branches = bst.Node(10)
    vals = range(11, 21)
    for val in vals:
        no_branches.insert(val)
    return no_branches


def test_built_no_branches_size(built_tree_no_branches):
    assert built_tree_no_branches.size() == 11


def test_built_no_branches_depth(built_tree_no_branches):
    assert built_tree_no_branches.depth() == 11


def test_built_no_branches_balance(built_tree_no_branches):
    assert built_tree_no_branches.balance() == -10


def test_built_tree_pre_order_dft(built_tree):
    expected = [10, 5, 3, 2, 4, 7, 6, 9, 15, 12, 11, 14, 20, 18, 22]
    actual = [node.value for node in list(built_tree.pre_order())]
    assert actual == expected


def test_no_branches_pre_order_dft(built_tree_no_branches):
    expected = range(10, 21)
    actual = [node.value for node in list(built_tree_no_branches.in_order())]
    assert actual == expected


def test_built_tree_in_order_dft(built_tree):
    expected = [2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 14, 15, 18, 20, 22]
    actual = [node.value for node in list(built_tree.in_order())]
    assert actual == expected


def test_no_branches_in_order_dft(built_tree_no_branches):
    expected = range(10, 21)
    actual = [node.value for node in list(built_tree_no_branches.in_order())]
    assert actual == expected


def test_built_tree_post_order_dft(built_tree):
    expected = [2, 4, 3, 6, 9, 7, 5, 11, 14, 12, 18, 22, 20, 15, 10]
    actual = [node.value for node in list(built_tree.post_order())]
    assert actual == expected


def test_no_branches_post_order_dft(built_tree_no_branches):
    expected = range(20, 9, -1)
    actual = [node.value for node in list(built_tree_no_branches.post_order())]
    assert actual == expected


def test_built_tree_bft(built_tree):
    expected = [10, 5, 15, 3, 7, 12, 20, 2, 4, 6, 9, 11, 14, 18, 22]
    actual = [node.value for node in list(built_tree.breadth_order())]
    assert actual == expected


def test_no_branches_bft(built_tree_no_branches):
    expected = range(10, 21)
    actual = [node.value for node in list(built_tree_no_branches.breadth_order())]
    assert actual == expected
