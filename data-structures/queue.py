from __future__ import unicode_literals
from queue_linked_list import LinkedList


class Queue(object):

    def __init__(self):
        self._linkedList = LinkedList()

    def enqueue(self, value):
        self._linkedList.insert(value)

    def dequeue(self):
            if self.size() == 0:
                raise IndexError
            else:
                return self._linkedList.pop()

    def size(self):
        return self._linkedList.size()

    def display(self):
        return self._linkedList.display()
