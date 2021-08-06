"""
Given an integer A.

Compute and return the square root of A.

If A is not a perfect square, return floor(sqrt(A)).

DO NOT USE SQRT FUNCTION FROM STANDARD LIBRARY.

NOTE: Do not use sort function from standard library. Users are expected to solve this in O(log(A)) time.



Input Format
The first and only argument given is the integer A.



Output Format
Return floor(sqrt(A))
"""


def sqrt(self, A):
        l, r = 0, A
        while l <= r:
            mid = (l+r)//2
            if mid * mid <= A:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans