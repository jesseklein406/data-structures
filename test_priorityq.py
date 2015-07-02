#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Pytest module for 'priorityq.py'
"""

from __future__ import unicode_literals
import pytest
from priorityq import PriorityQ, Item


@pytest.structure(scope="module")
def build_priorityq():
    built = PriorityQ()
    jim = Item("jim", 5)
    allen = Item("allen", 1)
    number2 = Item(2, 2)
    number3 = Item(3, 2)

    built.insert(jim)       # heapList = [0, 5]
    built.insert(allen)     # heapList = [0, 1, 5]
    built.insert(number2)   # heapList = [0, 1, 5, 2]
    built.insert(number3)   # heapList = [0, 1, 3, 2, 5]

    return built


@pytest.structure(scope="function")
def build_empty_q():
    empty = PriorityQ()

    return empty


def test_built_list(build_priorityq):
    assert build_priorityq.pqheap.heapList == [0, 1, 3, 2, 5]


def test_built_peek(build_priorityq):
    assert build_priorityq.peek().value == "allen"


def test_built_fifo(build_priorityq):
    build_priorityq.insert(Item("joshua", 1))   # heapList = [0, 1, 1, 2, 5, 3]
    first = build_priorityq.pop()
    assert first.value == "allen"


def test_next_priority(build_priorityq):
    assert build_priorityq.peek().value == "joshua"


def test_next_popped(build_priorityq):
    next = build_priorityq.pop()
    assert next.value == "joshua"


def test_new_list(build_priorityq):
    assert build_priorityq.pqheap.heapList == [0, 2, 3, 5]
