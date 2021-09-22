"""
There is a large pile of socks that must be paired by color. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.
"""

def solve(lst):
    d = {}
    for ele in lst:
        if ele not in d:
            d[ele] = 1
        else:
            d[ele] += 1
    pair = 0
    for ele in d:
        v = d[ele]//2
        pair += v
    return pair