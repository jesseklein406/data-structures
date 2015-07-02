#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import random

class Item(object):

    def __init__(self, value, priority):
        self.value = value
        self.priority = priority

    # Priority with lower values are higher priority than those
    # with higher values. E.g. Item with priority 1 is higher
    # t
    def higher_pri_than(self, item):
        return self.priority < item.priority


class PriorityQ(object):

    def __init__(self):
        self.pqheap = BinHeap()

    def insert(self, item):
        self.pqheap.push(item)

    def pop(self):
        return self.pqheap.pop()

    def peek(self):
        pass


class BinHeap(object):

    def __init__(self, iterable=None):
        # heap will start at index 1 of heapList.
        self.heapList = [0]
        self._size = 0

        # builds a heap from an iterable
        if iterable is not None:
            index = len(iterable) // 2
            self._size = len(iterable)
            self.heapList = self.heapList + list(iterable[:])
            while index > 0:
                self.pop_helper(index)
                index = index - 1

    def push_helper(self, index):
        while index // 2 > 0:
            if self.heapList[index].higher_pri_than(self.heapList[index // 2]):
                temp = self.heapList[index // 2]
                self.heapList[index // 2] = self.heapList[index]
                self.heapList[index] = temp
            index = index // 2

    # inserts value and rebuilds the heap
    def push(self, item):
        self.heapList.append(item)
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
                if (self.heapList[leftChildIndex].higher_pri_than(
                        self.heapList[rightChildIndex])):
                    smallestChild = leftChildIndex
                else:
                    smallestChild = rightChildIndex

            if self.heapList[smallestChild].higher_pri_than(self.heapList[index]):
                # self.heapList[index] > self.heapList[smallestChild]:
                temp = self.heapList[index]
                self.heapList[index] = self.heapList[smallestChild]
                self.heapList[smallestChild] = temp
            index = smallestChild
            leftChildIndex = 2 * index
            rightChildIndex = 2 * index + 1


pq = PriorityQ()
for i in range(9):
    r = random.randrange(57)
    print r
    item = Item(i, r)
    pq.insert(item)


l = pq.pqheap.heapList

for item in l:
    if type(item) is not int:
        print "priority:", item.priority, " ",

print '\n\n'

