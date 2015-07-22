# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class Node(object):

    size = 0

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.__class__.size += 1

    def insert(self, value):
        if value == self.value:
            return
        elif value < self.value:
            if self.left is None:
                self.left == Node(value)
            else:
                return self.left.insert(value)
        else:
            if self.right is None:
                return self.right == Node(value)
            else:
                return self.right.insert(value)

    def contains(self, value):
        if value == self.value:
            return True
        elif value < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(value)
        else:
            if self.right is None:
                return False
            else:
                return self.right.conains(value)

    def size(self):
        return self.__class__.size

    def depth(self):
        if self.left == None and self.right == None:
            return 1
        return max(depth(self.left), depth(self.right)) + 1

    def balance(self):
        return self.left.depth() - self.right.depth()
