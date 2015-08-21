"""Pytest file for linked_list.py

Run this with the command 'py.test test_linked_list.py'
"""


from __future__ import unicode_literals
import linked_list
import pytest


@pytest.fixture(scope='function')
def ll():
    ll = linked_list.LinkedList()
    return ll


def test_size_and_insert(ll):
    ll.insert(5)
    assert ll.size() == 1
    assert ll.head.value == 5


def test_insert_2(ll):
    ll.insert(5)
    ll.insert(6)
    assert ll.head.value == 6
    assert ll.head.next_node.value == 5


# search method

def test_search_value_in_list(ll):
    ll.insert(6)
    assert ll.search(6).value == 6
    assert ll.search(7) is None       # 7 is not in the list


def test_remove(ll):
    ll.insert(6)
    searched = ll.search(6)
    assert searched.value == 6
    ll.remove(searched)
    # import pdb; pdb.set_trace()
    assert ll.search(6) is None


def test_display(ll):
    ll.insert(6)
    assert ll.display() == (6,)


def test_pop(ll):
    ll.insert(6)
    assert ll.pop() == 6
    assert ll.size() == 0


def test_iterable():
    ll = linked_list.LinkedList([1, 2, 3])
    assert ll.size() == 3


def test_iterable_failure():
    with pytest.raises(TypeError):
        return linked_list.LinkedList(9)
