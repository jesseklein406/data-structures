#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class BinHeap(object):

    def __init__(self):
        # heap will start at index 1 of heapList.
        self.heapList = [0]
        self._size = 0

    def push_helper(self, index):
        while index // 2 > 0:
            if self.heapList[index] < self.heapList[index // 2]:
                temp = self.heapList[index // 2]
                self.heapList[index // 2] = self.heapList[index]
                self.heapList[index] = temp
            index = index // 2

    # inserts value and rebuilds the heap
    def push(self, val):
        self.heapList.append(val)
        self._size += 1
        self.push_helper(self._size)

    # removes the smallest element
    def pop(self):
        value = self.heapList[1]
        self.heapList[1] = self.heapList[self._size]
        self.heapList.pop()
        self._size -= 1
        self.pop_helper(1)

        return value

    def pop_helper(self, index):
        leftChildIndex = 2 * index
        rightChildIndex = 2 * index + 1

        while leftChildIndex <= self._size:
            if rightChildIndex > self._size:
                smallestChild = leftChildIndex
            else:
                if self.heapList[leftChildIndex] < self.heapList[rightChildIndex]:
                    smallestChild = leftChildIndex
                else:
                    smallestChild = rightChildIndex

            if self.heapList[index] > self.heapList[smallestChild]:
                temp = self.heapList[index]
                self.heapList[index] = self.heapList[smallestChild]
                self.heapList[smallestChild] = temp
            index = smallestChild
            leftChildIndex = 2 * index
            rightChildIndex = 2 * index + 1
