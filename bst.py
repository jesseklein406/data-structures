#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals


# use queue from queue assigment
class QueueNode(object):
    def __init__(self, value):
        self.value = value
        self.next_node = None


class Queue(object):
    def __init__(self, iterable=None):
        self.size = 0
        self.head = None

    def insert(self, val):
        new_node = QueueNode(val)
        current = self.head

        if current is None:
            self.head = new_node
            self.size += 1
        else:
            while current.next_node is not None:
                current = current.next_node
            current.next_node = new_node
            self.size += 1

    def pop(self):
        value = self.head.value
        self.head = self.head.next_node
        self.size -= 1
        return value


class Node(object):
    """
    A Node class that will create instances of nodes, all of which can
    represent the root of a binary search tree.
    """
    def __init__(self, value):
        """
        Make a new nodes object with a value given as the argument
        """
        self.value = value
        self.left = None    # initially set pointers to None
        self.right = None

    def insert(self, value):
        """
        Insert a new node into a tree with value given as argument if value
        is not present, else do nothing
        """
        if value == self.value:
            return   # if value exists, do nothing
        elif value < self.value:
            if self.left is None:
                self.left = Node(value)  # create value at empty pointer
            else:
                return self.left.insert(value)  # repeat for next node
        else:
            if self.right is None:
                self.right = Node(value)
            else:
                return self.right.insert(value)

    def contains(self, value):
        """
        Check a tree for a node with value given as argument, return True
        if the value is present, False if not
        """
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
                return self.right.contains(value)

    def size(self):
        """
        Return the number of nodes in a tree
        """
        l = self.left.size() if self.left else 0
        r = self.right.size() if self.right else 0
        return l + r + 1

    def depth(self):
        """
        Return the depth of the tree
        """
        l = self.left.depth() if self.left else 0
        r = self.right.depth() if self.right else 0
        return max(l, r) + 1

    def balance(self):
        """
        Return a positive balance if the root's left side is deeper,
        negative balance if the right side is deeper, and zero if
        the tree is balanced
        """
        l = self.left.depth() if self.left else 0
        r = self.right.depth() if self.right else 0
        return l - r

    # Depth first traverals
    def pre_order(self):
        """
        Call a pre-order depth first traversal generator.
        Return nodes in turn from generator.
        """
        parent_stack = []
        while parent_stack or self is not None:
            if self is not None:
                yield self
                # self is the symbol for the currently traversed node
                if self.right is not None:
                    parent_stack.append(self.right)
                self = self.left
            else:
                self = parent_stack.pop()

    def in_order(self):
        """
        Call an in-order depth first traversal generator.
        Return nodes in turn from generator.
        """
        parent_stack = []
        while parent_stack or self is not None:
            if self is not None:
                parent_stack.append(self)
                self = self.left
            else:
                self = parent_stack.pop()
                yield self
                self = self.right

    def post_order(self):
        """
        Call a post-order depth first traversal generator.
        Return nodes in turn from generator.
        """
        parent_stack = []
        last_node = None
        while parent_stack or self is not None:
            if self is not None:
                parent_stack.append(self)
                self = self.left
            else:
                peek = parent_stack[-1]
                if peek.right is not None and last_node is not peek.right:
                    self = peek.right
                else:
                    yield peek
                    last_node = parent_stack.pop()

    def breadth_order(self):
        """
        Call a breadth first traversal generator.
        Return nodes in turn from generator. Use a queue
        object to maintain first in first out order.
        """
        queue = Queue()   # queue class from above
        queue.insert(self)
        while queue.size is not 0:
            self = queue.pop()
            yield self
            if self.left is not None:
                queue.insert(self.left)
            if self.right is not None:
                queue.insert(self.right)

    def find_successor(self, val):
        while self.left:
            self = self.left
        return self

    def find_predecessor(self,val):
        while self.right:
            self = self.right
        return self

    def replace_node_in_parent(self, parent=None, new_node=None):
        if parent:
            if self == parent.left:
                parent.left = new_node
            else:
                parent.right = new_node

    def delete(self, value, parent=None):
        if value < self.value:
            self.left.delete(value, parent=self)
        elif value > self.value:
            self.right.delete(value, parent=self)
        else:
            if self.left and self.right:
                if self.balance() < 0:
                    replacement = self.right.find_successor()
                else:
                    replacement = self.left.find_predeessor()
                self.value = replacement.value
                replacement.delete(replacement.value)
            elif self.left:
                self.replace_node_in_parent(parent=parent, new_node=self.left)
            elif self.right:
                self.replace_node_in_parent(parent=parent, new_node=self.right)
            else:
                self.replace_node_in_parent(parent=parent, new_node=None)



if __name__ == '__main__':
    from timeit import Timer
    tree_root = Node(10)
    vals = [5, 15, 3, 7, 12, 20, 2, 4, 6, 9, 11, 14, 18, 25]
    for val in vals:
        tree_root.insert(val)

    no_branches = Node(10)
    vals = range(11, 25)
    for val in vals:
        no_branches.insert(val)

    print
    print "Time for optimally filled tree with 15 nodes to search for 15th node"
    print Timer(
        'tree_root.contains(25)',
        'from __main__ import tree_root'
    ).timeit(1000)

    print
    print "Time for tree with no branches with 15 nodes to search for 15th node"
    print Timer(
        'no_branches.contains(25)',
        'from __main__ import no_branches'
    ).timeit(1000)
    print
    print "This represents time for searching with 4 recursions vs 15 recursions,"
    print "or about a ~1/4 ratio"
