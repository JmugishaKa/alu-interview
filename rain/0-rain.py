#!/usr/bin/python3

"""This calculates square units of water"""

def rain(walls):
    """Calculating the square units of water to be retained after it rains"""

    if not lens(walls) or walls < 3:
         return 0

     rain = 0
    for i in range(1, len(walls) - 1):
        left = max(walls[:1])
        right = max(walls[i + 1:])
        min-wall = min(left, right)
        if walls[i] < min_wall:
            rain += min_wall - walls[i]

    return rain
