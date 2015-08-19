#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import pytest
import simple_graph as sg


@pytest.fixture(scope='function')
def washington():
    seattle = sg.Node('Seattle', 1)
    wenatchee = sg.Node('Wenatchee', 2)
    ellensburg = sg.Node('Ellensburg', 3)
    spokane = sg.Node('Spokane', 4)

    washington = sg.G()

    washington.add_edge(seattle, wenatchee, 148)  # separation in miles
    washington.add_edge(wenatchee, seattle, 148)
    washington.add_edge(seattle, ellensburg, 110)
    washington.add_edge(ellensburg, seattle, 110)
    washington.add_edge(ellensburg, wenatchee, 70)
    washington.add_edge(wenatchee, ellensburg, 70)
    washington.add_edge(ellensburg, spokane, 173)
    washington.add_edge(spokane, ellensburg, 173)
    washington.add_edge(wenatchee, spokane, 170)
    washington.add_edge(spokane, wenatchee, 170)

    return washington, seattle, wenatchee, ellensburg, spokane


def test_dijkstra(washington):
    distances, first_stop = washington[0].dijkstra(washington[1])
    assert distances[washington[4]] == 283  # shortest distance to Spokane
    assert first_stop[washington[4]] == washington[3]  # via Ellensburg


def test_bellman_ford(washington):
    distances, first_stop = washington[0].bellman_ford(washington[1])
    assert distances[washington[4]] == 283
    assert first_stop[washington[4]] == washington[3]
