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

    def _find_successor(self, parent=None):
        while self.left:
            parent = self
            self = self.left
        return self, parent

    def _find_predecessor(self, parent=None):
        while self.right:
            parent = self
            self = self.right
        return self, parent

    def delete(self, value, parent=None):
        if not self.contains(value):
            return None
        if value < self.value:
            self.left.delete(value, parent=self)
        elif value > self.value:
            self.right.delete(value, parent=self)
        else:
            if self.left or self.right:
                if self.balance() < 0:
                    replacement, r_parent = self.right._find_successor(parent=self)
                else:
                    replacement, r_parent = self.left._find_predecessor(parent=self)
                self.value = replacement.value
                replacement.delete(replacement.value, parent=r_parent)
            elif parent:
                if self == parent.left:
                    parent.left = None
                else:
                    parent.right = None

    def left_rotation(self):
        pivot = self.right
        self.right = pivot.left
        pivot.left = self

    def right_rotation(self):
        pivot = self.left
        self.left = pivot.right
        pivot.right = self

    def rebalance(self):
        """
        Rebalance a tree whose sides differ in depth by more than one
        """
        if self.balance() < -1:
            pivot = self.right
            if pivot.balance() <= 0:   # right right case
                self.left_rotation()
                pivot.rebalance()   # new root
            else:                   # right left case
                pivot_of_pivot = pivot.left
                pivot.right_rotation()
                self.right = pivot_of_pivot  # new root of subtree
                self.left_rotation()
                pivot_of_pivot.rebalance()   # new root
        elif self.balance() > 1:
            pivot = self.left
            if pivot.balance() >= 0:   # left left case
                self.right_rotation()
                pivot.rebalance()
            else:                      # left right case
                pivot_of_pivot = pivot.right
                pivot.left_rotation()
                self.left = pivot_of_pivot
                self.right_rotation()
                pivot_of_pivot.rebalance()

    def get_dot(self):
            """return the tree with root 'self' as a dot graph for visualization"""
            return "digraph G{\n%s}" % ("" if self.value is None else (
                "\t%s;\n%s\n" % (
                    self.value,
                    "\n".join(self._get_dot())
                )
            ))

    def _get_dot(self):
        """recursively prepare a dot graph entry for this node."""
        import random
        if self.left is not None:
            yield "\t%s -> %s;" % (self.value, self.left.value)
            for i in self.left._get_dot():
                yield i
        elif self.right is not None:
            r = random.randint(0, 1e9)
            yield "\tnull%s [shape=point];" % r
            yield "\t%s -> null%s;" % (self.value, r)
        if self.right is not None:
            yield "\t%s -> %s;" % (self.value, self.right.value)
            for i in self.right._get_dot():
                yield i
        elif self.left is not None:
            r = random.randint(0, 1e9)
            yield "\tnull%s [shape=point];" % r
            yield "\t%s -> null%s;" % (self.value, r)

    def save_render(self, savefile="tree.gv"):
            from graphviz import Source
            src = Source(self.get_dot())
            src.render(savefile)


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
