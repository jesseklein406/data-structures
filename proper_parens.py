#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Access the function 'proper_parens(str)' to determine
if a string is open, balanced, or broken
"""

from __future__ import unicode_literals


def proper_parens(parens_string):
    """Determine if a string is open, balanced, or broken

    Positional arguments:
    parens_string - input string to be evaluated
    """
    stack = []
    
    for char in parens_string:
        if char == "(":
            stack.append(char)
        elif char == ")":
            try:
                stack.pop()
            except IndexError:
                return -1

    if stack:
        return 1
    else:
        return 0
