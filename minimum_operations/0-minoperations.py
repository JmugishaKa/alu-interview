#!/usr/bin/python3

"""
Using a number n, we can use a method that calculates the fewest # of operations.

Prototype: def minOperations(n)
Return an integer
If n is not found or impossible to reach, returns 0
"""


def minOperations(n):
    if n <= 1:
        return 0

    i = 2
    while i * i <= n:
        if n % i == 0:
            return i + minOperations(n // i)
        i += 1

    return n
