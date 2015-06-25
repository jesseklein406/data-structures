# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pytest
import stack


value = [1, 2, 3, 4, 5]
foo = stack.Stack(value)


# init

# check instance is type 'stack'
def test_init_type():
    assert type(foo) == 'stack'

# check 'push' and 'pop' in dir(foo)
def test_init_push():
    assert 'push' in dir(foo)


def test_init_pop():
    assert 'pop' in dir(foo)

# check 'insert', 'size', 'search', 'remove', 'display' are not in dir(foo)
def test_init_insert():
    assert 'insert' not in dir(foo)


def test_init_size():
    assert 'size' not in dir(foo)


def test_init_search():
    assert 'search' not in dir(foo)


def test_init_remove():
    assert 'remove' not in dir(foo)


def test_init_display():
    assert 'display' not in dir(foo)


# pop

bar = foo.pop()

# check bar = 5
def test_pop_value():
    assert bar == 5


empty = stack.Stack([])

# assert empty.pop() raises Exception
def test_pop_empty():
    with pytest.raises(Exception):
        nothing = empty.pop()


# push

foo.push(5)

# check foo = stack.Stack(value)
def test_push_restore():
    assert foo == stack.Stack(value)
