#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Pytest file for 'binheap.py'
"""

from __future__ import unicode_literals
import pytest
import binheap


@pytest.fixture(scope="module")
def create_filled():
    filled_heap = binheap.BinHeap([1, 2, 3])
    return filled_heap


@pytest.fixture(scope="module")
def create_empty():
    empty_heap = binheap.BinHeap()
    return empty_heap


def test_heap_build(create_empty):
    create_empty.push(9)
    create_empty.push(7.7)
    create_empty.push(3)

    assert create_empty.heapList == [0, 3, 7.7, 9]


def test_heap_extend(create_empty):
    create_empty.push(1)    # [0, 1, 7.7, 9, 3]
    assert create_empty.heapList == [0, 1, 7.7, 9, 3]
    create_empty.push(8)   # [0, 1, 7.7, 9, 3, 8]
    create_empty.push(5)   # [0, 1, 5, 9, 3, 8, 7.7]

    assert create_empty.heapList == [0, 1, 5, 9, 3, 8, 7.7]
