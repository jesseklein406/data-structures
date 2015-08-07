#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import pytest
from random import shuffle
from radix import radix_integer, radix_string


@pytest.fixture(scope="function")
def presorted():
    presorted = range(10)
    return presorted


@pytest.fixture(scope="function")
def unsorted():
    unsorted = [8, 4, 6, 3, 5, 1, 9, 10, 2, 7]
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


@pytest.fixture(scope="function")
def mixed():
    mixed = [1, 'oops']
    return mixed


def test_presorted(presorted):
    sort = radix_integer(presorted)
    assert sort == range(10)


def test_unsorted(unsorted):
    sort = radix_integer(unsorted)
    assert sort == range(1, 11)


def test_binary(binary):
    sort = radix_integer(binary)
    assert sort == [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]


def test_one(one):
    sort = radix_integer(one)
    assert sort == [5]


def test_empty(empty):
    sort = radix_integer(empty)
    assert sort == []


def test_big(big):
    sort = radix_integer(big)
    assert sort == range(10000)


def test_mixed_1(mixed):
    with pytest.raises(AssertionError):
        radix_integer(mixed)


@pytest.fixture(scope="function")
def sorted_words():
    presorted = ['and', 'everything', 'is', 'okay']
    return presorted


@pytest.fixture(scope="function")
def unsorted_words():
    unsorted = ['the', 'quick', 'brown', 'fox']
    return unsorted


@pytest.fixture(scope="function")
def other_characters():
    characters = ['a space', 'ALLCAPS', 'brilliant!']
    return characters


@pytest.fixture(scope="function")
def one_word():
    one = ['one']
    return one


@pytest.fixture(scope="function")
def no_words():
    empty = []
    return empty


def test_sorted_words(sorted_words):
    sort = radix_string(sorted_words)
    assert sort == sorted_words


def test_unsorted_words(unsorted_words):
    sort = radix_string(unsorted_words)
    assert sort == ['brown', 'fox', 'quick', 'the']


def test_other_characters(other_characters):
    sort = radix_string(other_characters)
    assert sort == ['a space', 'brilliant!', 'ALLCAPS']


def test_one_word(one_word):
    sort = radix_string(one_word)
    assert sort == ['one']


def test_no_words(no_words):
    sort = radix_string(no_words)
    assert sort == []


def test_mixed_2(mixed):
    with pytest.raises(AssertionError):
        radix_string(mixed)
