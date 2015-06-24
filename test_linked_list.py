from __future__ import unicode_literals
import linked_list

# def func(x):
#     return x + 1

# def tdest_answer():
#     assert func(3) == 5


# init

a = linked_list.LinkedList()


def test_size():
    assert a.size is 0


def test_head():
    assert a.head is None


def test_init():
    assert type(a) is linked_list.LinkedList


