# -*- coding: utf-8 -*-
"""Test file for 'stack.py'

Run this file with pytest to test conditions
"""
from __future__ import unicode_literals
import pytest
import stack


@pytest.fixture(scope='function')
def foo():
    value = [1, 2, 3, 4, 5]
    foo = stack.Stack(value)
    return foo


def test_init_error():
    with pytest.raises(TypeError):
        return stack.Stack(5)


def test_pop_value(foo):
    assert foo.pop() == 5


def test_pop_empty(foo):
    """Assert empty.pop() raises Exception"""
    with pytest.raises(AttributeError):
        for i in range(6):
            foo.pop()


def test_push(foo):
    """Check foo.pop() = 5"""
    foo.push(6)
    assert foo._linkedList.head.value == 6


def test_preserve_iterable(foo):
    foo.push([6, 7, 8])
    foo._linkedList.head.value == [6, 7, 8]
