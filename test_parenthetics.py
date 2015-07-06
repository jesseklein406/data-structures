""" Tests for parenthetics.py
Run with pytest
"""
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pytest
import parenthetics


def test_empty():
    s = ""
    assert parenthetics.parens(s) == 0

def test_no_parens():
    s = 'no parens'
    assert parenthetics.parens(S) == 0


def test_open():
    s = "("
    assert parenthetics.parens(s) == 1


def test_open2():
    s = "((c(ab()d"
    assert parenthetics.parens(s) == 1


def test_balanced():
    s = "()()()"
    assert parenthetics.parens(s) == 0


def test_balanced2():
    s = "(((klmn)))k()((p))"
    assert parenthetics.parens(s) == 0


def test_broken():
    s = "()(q))"
    assert parenthetics.parens(s) == -1


def test_broken2():
    s = ")))(y(("
    assert parenthetics.parens(s) == -1
