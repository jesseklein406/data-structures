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


# * * * * *#
# Deletion #
# * * * * *#


@pytest.fixture(scope="function")
def small_tree():
    small_tree = bst.Node(10)
    small_tree.insert(2)
    small_tree.insert(18)
    return small_tree


@pytest.fixture(scope="function")
def unbalanced_tree():
    unbalanced_tree = bst.Node(10)
    unbalanced_tree.insert(2)
    unbalanced_tree.insert(18)
    unbalanced_tree.insert(15)
    return unbalanced_tree


def test_leaf_in_built_tree(built_tree):
    built_tree.delete(4)
    assert built_tree.size() == 14   # was 15
    assert not built_tree.contains(4)
    three = built_tree.left.left
    assert three.right is None


def test_node_with_two_children(built_tree):
    built_tree.delete(7)
    assert built_tree.size() == 14
    assert not built_tree.contains(7)
    six = built_tree.left.right
    assert six.left is None


def test_node_with_one_child(built_tree):
    built_tree.delete(7)   # from above
    built_tree.delete(6)
    assert built_tree.size() == 13
    assert not built_tree.contains(6)
    assert built_tree.left.right.value == 9  # moved into old 6 spot


def test_value_not_in_tree(built_tree):
    built_tree.delete(21)
    assert built_tree.size() == 15  # unchanged


def test_unbranched_tree(built_tree_no_branches):
    built_tree_no_branches.delete(15)
    assert built_tree_no_branches.size() == 10   # was 11
    fourteen = built_tree_no_branches.right.right.right.right
    assert fourteen.right.value == 16


def test_unbranched_tree_leaf(built_tree_no_branches):
    built_tree_no_branches.delete(20)
    assert built_tree_no_branches.size() == 10   # was 11
    child = built_tree_no_branches.right  # 11

    for i in range(8):  # returns 19
        child = child.right

    assert child.right is None and child.left is None


def test_unbalanced_tree(unbalanced_tree):
    unbalanced_tree.delete(10)  # root
    assert unbalanced_tree.value == 15  # new root
    assert unbalanced_tree.balance() == 0  # new balance


def test_small_tree(small_tree):
    small_tree.delete(10)  # root
    assert small_tree.value == 2   # new root
    small_tree.delete(2)   # root
    assert small_tree.value == 18   # new root, only node
    assert small_tree.left is None and small_tree.right is None


# * * * * * #
# Rebalance #
# * * * * * #


@pytest.fixture(scope="function")
def left_rot_case():
    left_rot_case = bst.Node(2)
    left_rot_case.insert(1)
    left_rot_case.insert(4)
    left_rot_case.insert(3)
    left_rot_case.insert(5)

    return left_rot_case


@pytest.fixture(scope="function")
def right_rot_case():
    right_rot_case = bst.Node(4)
    right_rot_case.insert(2)
    right_rot_case.insert(5)
    right_rot_case.insert(1)
    right_rot_case.insert(3)

    return right_rot_case


@pytest.fixture(scope="function")
def left_left_case():
    left_left_case = bst.Node(6)
    left_left_case.insert(4)
    left_left_case.insert(7)
    left_left_case.insert(2)
    left_left_case.insert(5)
    left_left_case.insert(1)
    left_left_case.insert(3)

    return left_left_case


@pytest.fixture(scope="function")
def right_right_case():
    right_right_case = bst.Node(2)
    right_right_case.insert(1)
    right_right_case.insert(4)
    right_right_case.insert(3)
    right_right_case.insert(6)
    right_right_case.insert(5)
    right_right_case.insert(7)

    return right_right_case


@pytest.fixture(scope="function")
def left_right_case():
    left_right_case = bst.Node(6)
    left_right_case.insert(2)
    left_right_case.insert(7)
    left_right_case.insert(1)
    left_right_case.insert(4)
    left_right_case.insert(3)
    left_right_case.insert(5)

    return left_right_case


@pytest.fixture(scope="function")
def right_left_case():
    right_left_case = bst.Node(2)
    right_left_case.insert(1)
    right_left_case.insert(6)
    right_left_case.insert(4)
    right_left_case.insert(7)
    right_left_case.insert(3)
    right_left_case.insert(5)

    return right_left_case


def test_left_rotation(left_rot_case):
    # 4 is pivot
    four = left_rot_case.right
    left_rot_case.left_rotation()

    # 4 is now root
    assert four.right.value == 5
    assert four.left.value == 2
    assert four.balance() == 1
    assert four.depth() == 3


def test_right_rotation(right_rot_case):
    # 2 is pivot
    two = right_rot_case.left
    right_rot_case.right_rotation()

    # 2 is now root
    assert two.right.value == 4
    assert two.left.value == 1
    assert two.balance() == -1
    assert two.depth() == 3


def test_left_left_rebalance(left_left_case):
    # 4 is pivot
    four = left_left_case.left
    left_left_case.rebalance()

    # 4 is now root
    assert four.right.value == 6
    assert four.left.value == 2
    assert four.balance() == 0
    assert four.depth() == 3
    assert four.size() == 7


def test_right_right_rebalance(right_right_case):
    # 4 is pivot
    four = right_right_case.right
    right_right_case.rebalance()

    # 4 is now root
    assert four.right.value == 6
    assert four.left.value == 2
    assert four.balance() == 0
    assert four.depth() == 3
    assert four.size() == 7


def test_left_right_rebalance(left_right_case):
    # 4 is pivot
    four = left_right_case.left.right
    left_right_case.rebalance()

    # 4 is now root
    assert four.right.value == 6
    assert four.left.value == 2
    assert four.balance() == 0
    assert four.depth() == 3
    assert four.size() == 7


def test_right_left_rebalance(right_left_case):
    # 4 is pivot
    four = right_left_case.right.left
    right_left_case.rebalance()

    # 4 is now root
    assert four.right.value == 6
    assert four.left.value == 2
    assert four.balance() == 0
    assert four.depth() == 3
    assert four.size() == 7


def test_rebalance_unbranched(built_tree_no_branches):
    # 15 is pivot
    fifteen = built_tree_no_branches.right.right.right.right.right
    built_tree_no_branches.rebalance()

    # 15 is now root
    assert fifteen.right.value == 16
    assert fifteen.left.value == 14
    assert fifteen.balance() == 0
    assert fifteen.depth() == 6
    assert fifteen.size() == 11


def test_rebalance_balanced_tree(built_tree):
    built_tree.rebalance()

    # no change
    assert built_tree.right.value == 15
    assert built_tree.left.value == 5
    assert built_tree.balance() == 0
    assert built_tree.depth() == 4
    assert built_tree.size() == 15
