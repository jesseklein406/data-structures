#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from hash import Hash
import pytest
from time import time


def test_errors():
    ht = Hash()

    with pytest.raises(KeyError):
        ht.get("key")

    with pytest.raises(TypeError):
        ht.set(5, 5)


with open('/usr/share/dict/words') as fh:
    words = fh.read().split()


@pytest.fixture(scope='function')
def hash_256():
    start = time()

    hash_256 = Hash(256)

    for word in words:
        hash_256.set(word, word)

    end = time()

    print "\n256 Fixture: ", end - start

    return hash_256


@pytest.fixture(scope='function')
def hash_512():
    start = time()

    hash_512 = Hash(512)

    for word in words:
        hash_512.set(word, word)

    end = time()

    print "512 Fixture: ", end - start

    return hash_512


@pytest.fixture(scope='function')
def hash_1024():
    start = time()

    hash_1024 = Hash(1024)

    for word in words:
        hash_1024.set(word, word)

    end = time()

    print "1024 Fixture: ", end - start

    return hash_1024


@pytest.fixture(scope='function')
def hash_4096():
    start = time()

    hash_4096 = Hash(4096)

    for word in words:
        hash_4096.set(word, word)

    end = time()

    print "4096 Fixture: ", end - start

    return hash_4096


def test_all_in_256(hash_256):
    start = time()

    for word in words:
        assert hash_256.get(word) == word

    end = time()

    print "256 lookup: ", end - start


def test_all_in_512(hash_512):
    start = time()

    for word in words:
        assert hash_512.get(word) == word

    end = time()

    print "512 lookup: ", end - start


def test_all_in_1024(hash_1024):
    start = time()

    for word in words:
        assert hash_1024.get(word) == word

    end = time()

    print "1024 lookup: ", end - start


def test_all_in_4096(hash_4096):
    start = time()

    for word in words:
        assert hash_4096.get(word) == word

    end = time()

    print "4096 lookup: ", end - start
