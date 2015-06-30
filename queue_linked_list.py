from __future__ import unicode_literals


class Node(object):

    def __init__(self, value):
        self.value = value
        self.next_node = None


class LinkedList(object):

    def __init__(self, iterable=None):
        self.sizeOfList = 0
        self.head = None

        if iterable is not None:
            for item in iterable:
                self.insert(item)

    def insert(self, val):
        new_node = Node(val)
        current = self.head

        if current is None:
            self.head = new_node
            self.sizeOfList += 1
        else:
            while current.next_node is not None:
                current = current.next_node
            current.next_node = new_node
            self.sizeOfList += 1


    def pop(self):
        value = self.head.value
        self.head = self.head.next_node
        self.sizeOfList -= 1
        return value

    def size(self):
        return self.sizeOfList

    def display(self):
        current = self.head
        result = ()
        while current is not None:
            result += (current.value,)
            current = current.next_node
        return result
        