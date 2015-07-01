#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
class BinHeap(object):

    def __init__(self):
        self.heapList = [0]
        self._size = 0

    def insert_helper(self, index):
        while index // 2 > 0:
            if self.heapList[index] < self.heapList[index // 2]:
                temp = self.heapList[index // 2]
                self.heapList[index // 2] = self.heapList[index]
                self.heapList[index] = temp
            index = index // 2

    def insert(self, val):
        self.heapList.append(val)
        self._size += 1
        self.insert_helper(self._size)
