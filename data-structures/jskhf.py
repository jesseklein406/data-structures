#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import dll
import pytest


#@pytest.fixture(scope="function")
def create_lone_node():
    lone_node = dll.Node("test node")

    return lone_node


#@pytest.fixture(scope="function")
def create_empty():
    empty_dll = dll.Dll()

    return empty_dll


#@pytest.fixture(scope="function")
def create_inserted_dll():
    inserted_dll = dll.Dll()

    for i in range(1, 6):
        inserted_dll.insert(i)

    return inserted_dll


#@pytest.fixture(scope="function")
def create_appended_dll():
    appended_dll = dll.Dll()

    for i in range(1, 6):
        appended_dll.append(i)

    return appended_dll


#@pytest.fixture(scope="function")
def create_mirrored_dll():
    mirrored_dll = dll.Dll()

    for i in range(1, 6):
        mirrored_dll.insert(i)
        mirrored_dll.append(i)

    return mirrored_dll


def test_node_value():
    assert create_lone_node().val == "test node"


def test_node_next():
    assert create_lone_node().next_node is None


def test_node_prev():
    assert create_lone_node().prev_node is None


def test_empty_size():
    assert create_empty().sizeOfList is 0


def test_empty_head():
    assert create_empty().head is None


def test_empty_tail():
    assert create_empty().tail is None


def test_inserted_length():
    assert create_inserted_dll().sizeOfList is 5


def test_inserted_head_val():
    assert create_inserted_dll().head.val is 5


def test_inserted_head_next():
    assert create_inserted_dll().head.next.val is 4


def test_inserted_head_prev():
    assert create_inserted_dll().head.prev is None


def test_inserted_tail_val():
    assert create_inserted_dll().tail.val is 1


def test_inserted_tail_next():
    assert create_inserted_dll().tail.next is None


def test_inserted_tail_prev():
    assert create_inserted_dll().tail.prev.val is 2


def test_appended_length():
    assert create_appended_dll().sizeOfList is 5


def test_appended_head_val():
    assert create_appended_dll().head.val is 1


def test_appended_head_next():
    assert create_appended_dll().head.next.val is 2


def test_appended_head_prev():
    assert create_appended_dll().head.prev is None


def test_appended_tail_val():
    assert create_appended_dll().tail.val is 5


def test_appended_tail_next():
    assert create_appended_dll().tail.next is None


def test_appended_tail_prev():
    assert create_appended_dll().tail.prev.val is 4


def test_pop_return(create_objects):
    assert inserted_dll.pop() is 5


def test_pop_new_size(create_objects):
    inserted_dll.pop()
    assert inserted_dll.sizeOfList is 4


def test_pop_new_head_val(create_objects):
    inserted_dll.pop()
    assert inserted_dll.head.val is 4


def test_pop_new_head_next(create_objects):
    inserted_dll.pop()
    assert inserted_dll.head.next.val is 3


def test_pop_new_head_prev(create_objects):
    inserted_dll.pop()
    assert inserted_dll.head.prev is None


def test_pop_empty(create_objects):
    with pytest.raises(IndexError):
        empty_dll.pop()


def test_shift_return(create_objects):
    inserted_dll.shift() is 1


def test_shift_new_size(create_objects):
    inserted_dll.shift()
    assert inserted_dll.sizeOfList is 4


def test_shift_new_tail_val(create_objects):
    inserted_dll.shift()
    assert inserted_dll.tail.val is 2


def test_shift_new_tail_next(create_objects):
    inserted_dll.shift()
    assert inserted_dll.tail.next is None


def test_shift_new_tail_prev(create_objects):
    inserted_dll.shift()
    assert inserted_dll.tail.prev.val is 3


def test_shift_empty(create_objects):
    with pytest.raises(IndexError):
        empty_dll.pop()


def test_remove_size(create_objects):
    mirrored_dll.remove(5)
    assert mirrored_dll.sizeOfList is 9


def test_remove_head_val(create_objects):
    mirrored_dll.remove(5)
    assert mirrored_dll.head.val is 4


def test_remove_head_next(create_objects):
    mirrored_dll.remove(5)
    assert mirrored_dll.head.next.val is 3


def test_remove_head_prev(create_objects):
    mirrored_dll.remove(5)
    assert mirrored_dll.head.prev is None


def test_remove_tail_val(create_objects):
    mirrored_dll.remove(5)
    assert mirrored_dll.tail.val is 5


def test_remove_tail_next(create_objects):
    mirrored_dll.remove(5)
    assert mirrored_dll.tail.next is None


def test_remove_tail_prev(create_objects):
    mirrored_dll.remove(5)
    assert mirrored_dll.tail.prev.val is 4


def test_remove_empty(create_object):
    with pytest.raises(ValueError):
        empty_dll.remove(5)
