#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import pytest
from random import shuffle
from quick import quick


@pytest.fixture(scope="function")
def presorted():
    presorted = range(10)
    return presorted


@pytest.fixture(scope="function")
def unsorted():
    unsorted = [8, 4, 6, 3, 5, 1, 9, -3, 10, 2, 5.5, 7]
    return unsorted


@pytest.fixture(scope="function")
def binary():
    binary = [1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0]
    return binary


@pytest.fixture(scope="function")
def one():
    one = [5]
    return one


@pytest.fixture(scope="function")
def empty():
    empty = []
    return empty


@pytest.fixture(scope="function")
def big():
    big = range(10000)
    shuffle(big)
    return big


def test_presorted(presorted):
    sort = quick(presorted)
    assert sort == range(10)


def test_unsorted(unsorted):
    sort = quick(unsorted)
    assert sort == [-3, 1, 2, 3, 4, 5, 5.5, 6, 7, 8, 9, 10]


def test_binary(binary):
    sort = quick(binary)
    assert sort == [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]


def test_one(one):
    sort = quick(one)
    assert sort == [5]


def test_empty(empty):
    sort = quick(empty)
    assert sort == []


def test_big(big):
    sort = quick(big)
    assert sort == range(10000)
