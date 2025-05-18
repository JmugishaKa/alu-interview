#!/usr/bin/python3

"""Sample steps using a loop"""

def minOperations(n):
    if n <= 1:
        return 0

    i = 2
    while i * i <= n:
        if n % i == 0:
            return i + minOperations(n // i)
        i += 1

    return n
