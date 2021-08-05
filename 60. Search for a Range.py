"""
Given a sorted array of integers A(0 based index) of size N, find the starting and ending position of a given integar B in array A.

Your algorithm’s runtime complexity must be in the order of O(log n).

Return an array of size 2, such that first element = starting position of B in A and second element = ending position of B in A, if B is not found in A return [-1, -1].
"""


def searchRange(self, A, B):
        if B in A:
            c = A.index(B)
            d = A.count(B)
            return [c, c+d-1]
        return [-1,-1]