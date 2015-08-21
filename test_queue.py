#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A series of pytest tests to test the quality
of our Queue class and its methods
"""

from __future__ import unicode_literals
import pytest
import queue


@pytest.fixture(scope="function")
def create_queue(request):
    """Create a queue with numbers 1 - 5
    """
    new_queue = queue.Queue()
    for i in range(1, 6):
        new_queue.enqueue(i)
    return new_queue


def test_dequeue(create_queue):
    """Test that the queue shrinks and returns first in
    """
    first_queue = create_queue
    first_val = first_queue.dequeue()
    assert first_val is 1
    assert first_queue.size() is 4


def test_enqueue(create_queue):
    """Test that the queue grows and returns first in
    """
    second_queue = create_queue
    second_queue.enqueue(6)
    assert second_queue.size() is 6

    for i in range(5):
        second_queue.dequeue()

    last_val = second_queue.dequeue()
    assert last_val is 6


def test_empty(create_queue):
    """Test that empty queue size method returns 0 and dequeue raises IndexError
    """
    empty = queue.Queue()
    assert empty.size() is 0
    with pytest.raises(IndexError):
        empty.dequeue()
