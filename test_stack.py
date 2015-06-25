# -*- coding: utf-8 -*-
"""Test file for 'stack.py'

Run this file with pytest to test conditions
"""
from __future__ import unicode_literals
import pytest
import stack


value = [1, 2, 3, 4, 5]
foo = stack.Stack(value)


# init

def test_init_type():
    """Check instance is type 'stack'"""
    assert type(foo) == stack.Stack


def test_init_push():
    """Check 'push' in dir(foo)"""
    assert 'push' in dir(foo)


def test_init_pop():
    """Check 'pop' in dir(foo)"""
    assert 'pop' in dir(foo)


def test_init_insert():
    """Check 'insert' is not in dir(foo)"""
    assert 'insert' not in dir(foo)


def test_init_size():
    """Check 'size' is not in dir(foo)"""
    assert 'size' not in dir(foo)


def test_init_search():
    """Check 'search' is not in dir(foo)"""
    assert 'search' not in dir(foo)


def test_init_remove():
    """Check 'remove' is not in dir(foo)"""
    assert 'remove' not in dir(foo)


def test_init_display():
    """Check 'display' is not in dir(foo)"""
    assert 'display' not in dir(foo)


# pop

bar = foo.pop()


def test_pop_value():
    """Check bar = 5"""
    assert bar == 5


empty = stack.Stack([])


def test_pop_empty():
    """Assert empty.pop() raises Exception"""
    with pytest.raises(AttributeError):
        nothing = empty.pop()


# push

foo.push(bar)


def test_push_restore():
    """Check foo.pop() = 5"""
    assert foo.pop() == 5
