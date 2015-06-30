from __future__ import unicode_literals


class Node(object):

    def __init__(self, value):
        self.value = value
        self.next_node = None


class LinkedList(object):

    def __init__(self):
        self.sizeOfList = 0
        self.head = None

    def insert(self, val):
        new_node = Node(val)
        new_node.next_node = self.head
        self.head = new_node
        self.sizeOfList += 1
        print "head is now", self.head.value

    def pop(self):
        val = self.head.value
        self.head = self.head.next_node
        self.sizeOfList -= 1
        return val

    def size(self):
        return self.sizeOfList

    def search(self, val):
        current = self.head

        while current is None:
            if current.value == val:
                return current
            current = current.next_node

    def remove(self,node):
        previous = self.head
        current = self.head

        if current is node:
            self.head = current.next_node
            self.sizeOfList -= 1
        else:
            while current is not None and not (current is node):
                previous = current
                current = current.next_node
              
            if current is node:
                previous.next_node = current.next_node
                self.sizeOfList -=1

    def display(self):
        current = self.head
        result = ()
        while current != None:
            result += (current.value,) 
            current = current.next_node
        return result    

