#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Create a simple hash table using class Hash
"""

from __future__ import unicode_literals


class Hash(object):
    """A simple hash table using sum of character ord() values as hash algorithm

    Methods:
    get - lookup values in hash table
    set - set values in hash table
    """
    def __init__(self, buckets=1024):
        """Make a new hash table

        Keyword arg:
        buckets - numbers of buckets to store hashed keys, default is 1024
        """
        self.table = [[] for i in range(buckets)]
        self.buckets = buckets

    def hash(self, key):
        """Hash algorithm using sum of character ord() values

        Positional arg:
        key - lookup key for key value pair
        """
        hash_key = sum([ord(c) for c in key])
        return hash_key % self.buckets

    def _get_bucket(self, key):
        index = self.hash(key)
        return self.table[index]

    def _get_tuple(self, key):
        bucket = self._get_bucket(key)

        for i, pair in enumerate(bucket):
            k, v = pair
            if key == k:
                return i, v

        return -1, None

    def get(self, key):
        """Lookup a value from key

        Positional arg:
        key - lookup key for key value pair
        """
        i, v = self._get_tuple(key)
        if i == -1:
            raise KeyError('Key does not exist')

        return v

    def set(self, key, value):
        """Set a new key value pair

        Positional args:
        key - lookup key for key value pair, must be string
        value - value associated with key
        """
        if type(key) is not str:
            raise TypeError('Key must be string!')

        bucket = self._get_bucket(key)
        i, v = self._get_tuple(key)
        if i >= 0:
            bucket[i] = key, value   # update value of key
        else:
            bucket.append((key, value))
