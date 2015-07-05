#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test suite for proper_parens function
"""

from __future__ import unicode_literals
import pytest
from proper_parens import proper_parens


@pytest.fixture(scope="function")
def create_string():
    some_text = "some text"
    return some_text


def test_empty():
    assert proper_parens("") is 0


def test_start(create_string):
    assert proper_parens(create_string) is 0


def test_first_open(create_string):
    create_string = "{}(".format(create_string)   # "...("
    assert proper_parens(create_string) is 1


def test_second_open(create_string):
    create_string = "{}((".format(create_string)   # "...(("
    assert proper_parens(create_string) is 1


def test_still_open(create_string):
    create_string = "{}(()".format(create_string)   # "...(()"
    assert proper_parens(create_string) is 1


def test_first_balanced(create_string):
    create_string = "{}(())".format(create_string)   # "...(())"
    assert proper_parens(create_string) is 0


def test_next_open(create_string):
    create_string = "{}(())(".format(create_string)   # "...(())("
    assert proper_parens(create_string) is 1


def test_second_balanced(create_string):
    create_string = "{}(())()".format(create_string)   # "...(())()"
    assert proper_parens(create_string) is 0


def test_broken(create_string):
    create_string = "{}(())())".format(create_string)   # "...(())())"
    assert proper_parens(create_string) is -1


def test_text_1():
    text_1 = "This string( is open"
    assert proper_parens(text_1) is 1


def test_text_2():
    text_2 = "This string( is) balanced"
    assert proper_parens(text_2) is 0


def test_text_3():
    text_3 = "This string( is) bro)ken"
    assert proper_parens(text_3) is -1
