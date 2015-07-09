#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import dll
import pytest


@pytest.fixture(scope="function")
def create_lone_node():
    lone_node = dll.Node("test node")

    return lone_node


@pytest.fixture(scope="function")
def create_empty():
    empty_dll = dll.Dll()

    return empty_dll


@pytest.fixture(scope="function")
def create_inserted_dll():
    inserted_dll = dll.Dll()

    for i in range(1, 6):
        inserted_dll.insert(i)

    return inserted_dll


@pytest.fixture(scope="function")
def create_appended_dll():
    appended_dll = dll.Dll()

    for i in range(1, 6):
        appended_dll.append(i)

    return appended_dll


@pytest.fixture(scope="function")
def create_mirrored_dll():
    mirrored_dll = dll.Dll()

    for i in range(1, 6):
        mirrored_dll.insert(i)
        mirrored_dll.append(i)

    return mirrored_dll


def test_node_value(create_lone_node):
    assert create_lone_node.val == "test node"


def test_node_next(create_lone_node):
    assert create_lone_node.next_node is None


def test_node_prev(create_lone_node):
    assert create_lone_node.prev_node is None


def test_empty_size(create_empty):
    assert create_empty.sizeOfList is 0


def test_empty_head(create_empty):
    assert create_empty.head is None


def test_empty_tail(create_empty):
    assert create_empty.tail is None


def test_inserted_length(create_inserted_dll):
    assert create_inserted_dll.sizeOfList is 5


def test_inserted_head_val(create_inserted_dll):
    assert create_inserted_dll.head.val is 5


def test_inserted_head_next(create_inserted_dll):
    assert create_inserted_dll.head.next_node.val is 4


def test_inserted_head_prev(create_inserted_dll):
    assert create_inserted_dll.head.prev_node is None


def test_inserted_tail_val(create_inserted_dll):
    assert create_inserted_dll.tail.val is 1


def test_inserted_tail_next(create_inserted_dll):
    assert create_inserted_dll.tail.next_node is None


def test_inserted_tail_prev(create_inserted_dll):
    assert create_inserted_dll.tail.prev_node.val is 2


def test_appended_length(create_appended_dll):
    assert create_appended_dll.sizeOfList is 5


def test_appended_head_val(create_appended_dll):
    assert create_appended_dll.head.val is 1


def test_appended_head_next(create_appended_dll):
    assert create_appended_dll.head.next_node.val is 2


def test_appended_head_prev(create_appended_dll):
    assert create_appended_dll.head.prev_node is None


def test_appended_tail_val(create_appended_dll):
    assert create_appended_dll.tail.val is 5


def test_appended_tail_next(create_appended_dll):
    assert create_appended_dll.tail.next_node is None


def test_appended_tail_prev(create_appended_dll):
    assert create_appended_dll.tail.prev_node.val is 4


def test_pop_return(create_inserted_dll):
    assert create_inserted_dll.pop() is 5


def test_pop_new_size(create_inserted_dll):
    create_inserted_dll.pop()
    assert create_inserted_dll.sizeOfList is 4


def test_pop_new_head_val(create_inserted_dll):
    create_inserted_dll.pop()
    assert create_inserted_dll.head.val is 4


def test_pop_new_head_next(create_inserted_dll):
    create_inserted_dll.pop()
    assert create_inserted_dll.head.next_node.val is 3


def test_pop_new_head_prev(create_inserted_dll):
    create_inserted_dll.pop()
    assert create_inserted_dll.head.prev_node is None


def test_pop_empty(create_empty):
    with pytest.raises(IndexError):
        create_empty.pop()


def test_shift_return(create_inserted_dll):
    create_inserted_dll.shift() is 1


def test_shift_new_size(create_inserted_dll):
    create_inserted_dll.shift()
    assert create_inserted_dll.sizeOfList is 4


def test_shift_new_tail_val(create_inserted_dll):
    create_inserted_dll.shift()
    assert create_inserted_dll.tail.val is 2


def test_shift_new_tail_next(create_inserted_dll):
    create_inserted_dll.shift()
    assert create_inserted_dll.tail.next_node is None


def test_shift_new_tail_prev(create_inserted_dll):
    create_inserted_dll.shift()
    assert create_inserted_dll.tail.prev_node.val is 3


def test_shift_empty(create_empty):
    with pytest.raises(IndexError):
        create_empty.pop()


def test_remove_size(create_mirrored_dll):
    create_mirrored_dll.remove(5)
    assert create_mirrored_dll.sizeOfList is 9


def test_remove_head_val(create_mirrored_dll):
    create_mirrored_dll.remove(5)
    assert create_mirrored_dll.head.val is 4


def test_remove_head_next(create_mirrored_dll):
    create_mirrored_dll.remove(5)
    assert create_mirrored_dll.head.next_node.val is 3


def test_remove_head_prev(create_mirrored_dll):
    create_mirrored_dll.remove(5)
    assert create_mirrored_dll.head.prev_node is None


def test_remove_tail_val(create_mirrored_dll):
    create_mirrored_dll.remove(5)
    assert create_mirrored_dll.tail.val is 5


def test_remove_tail_next(create_mirrored_dll):
    create_mirrored_dll.remove(5)
    assert create_mirrored_dll.tail.next_node is None


def test_remove_tail_prev(create_mirrored_dll):
    create_mirrored_dll.remove(5)
    assert create_mirrored_dll.tail.prev_node.val is 4


def test_remove_empty(create_empty):
    with pytest.raises(ValueError):
        create_empty.remove(5)
