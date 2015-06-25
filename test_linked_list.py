"""Pytest file for linked_list.py

Run this with the command 'py.test test_linked_list.py'
"""


from __future__ import unicode_literals
import linked_list
import copy


# init method

a = linked_list.LinkedList()


def test_init_size():
    assert a.sizeOfList is 0
    assert type(a.sizeOfList) is int


def test_init_head():
    assert a.head is None


def test_init_type():
    assert type(a) is linked_list.LinkedList


# insert method

b = copy.copy(a)   # make a copy every time a change is made
b.insert(5)        # so the test can handle different values


def test_insert_size():
    assert b.sizeOfList is 1


def test_insert_head():
    assert b.head.value is 5


def test_insert_next():
    assert b.head.next_node is None


c = copy.copy(b)
c.insert(6)


def test_insert_new_size():
    assert c.sizeOfList is 2


def test_insert_new_head():
    assert c.head.value is 6


def test_insert_pointer():
    assert c.head.next_node.value is 5


# size method

def test_size():
    assert c.size() is 2


# search method

def test_search_value_in_list():
    assert c.search(5).value is 5


def test_search_value_not_in_list():
    assert c.search(7) is None       # 7 is not in the list


# remove method

d = copy.copy(c)
d.remove(d.search(6))


def test_remove_value():
    assert d.search(6) is None


def test_remove_size():
    assert d.size() is 1


# display method

def test_display():
    assert d.display() == (5,)    # test to make sure they are equivalent


# pop method

e = copy.copy(d)
f = e.pop()


def test_pop_size():
    assert e.size() is 0


def test_pop_return():
    assert f is 5
