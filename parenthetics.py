# -*- coding: utf-8 -*-
from __future__ import unicode_literals


"""
The parens() function takes in a string containing O or more parentheses
Returns: - 0 if the parentheses are balanced: the opening parentheses,
           '(', is the first parentheses in the string and the number of
            opening, '(', and number of closing ')' parentheses are equal
         - 1 if there are open parentheses that are not closed
         - -1 if a closing parentheses has not bee proceeded by one that
           that opens

"""


def parens(astring):
    parens_list = []

    for char in astring:
        if char == '(':
            parens_list.append(char)
        elif char == ')':
            try:
                parens_list.pop()
            except Exception:
                return -1
    if len(parens_list) != 0:
        return 1
    elif len(parens_list) == 0:
        return 0
