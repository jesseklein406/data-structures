from __future__ import unicode_literals


class Node(object):

    def __init__(self, value):
        self.value = value
        self.next_node = None


class LinkedList(object):

    def __init__(self, iterable=None):
        self.sizeOfList = 0
        self.head = None
        self.tail = None

        if iterable is not None:
            for item in iterable:
                self.insert(item)

    def insert(self, val):
        new_node = Node(val)

        if self.sizeOfList == 0:
            self.head = self.tail = new_node
            self.sizeOfList += 1
        else:
            self.tail.next_node = new_node
            self.tail = new_node
            self.sizeOfList += 1

    def pop(self):
        current = self.head
        previous = None
        val = self.tail.value

        if self.sizeOfList  == 1:
            self.head = self.tail = None
            self.sizeOfList -= 1
            return val
        else:
            while current is not self.tail:
                previous = current
                current = current.next_node
            self.tail = previous
            previous.next_node = None
            self.sizeOfList -= 1
            return val

    def size(self):
        return self.sizeOfList

    def display(self):
        current = self.head
        result = ()
        while current is not None:
            result += (current.value,)
            current = current.next_node
        return result

