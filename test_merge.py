#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import pytest
import random
from merge import merge_sort


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
    random.shuffle(big)
    return big


def test_unsorted(unsorted):
    merge_sort(unsorted)
    assert unsorted == [-3, 1, 2, 3, 4, 5, 5.5, 6, 7, 8, 9, 10]


def test_binary(binary):
    merge_sort(binary)
    assert binary == [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]


def test_one(one):
    merge_sort(one)
    assert one == [5]


def test_empty(empty):
    merge_sort(empty)
    assert empty == []


def test_big(big):
    merge_sort(big)
    assert big == range(10000)


def test_immutable():
    with pytest.raises(TypeError):
        merge_sort("nope")
