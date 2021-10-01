"""
Problem Description

Given an integer array A of size N, find the first repeating element in it.

We need to find the element that occurs more than once and whose index of first occurrence is smallest.

If there is no repeating element, return -1.



Problem Constraints
1 <= N <= 105

1 <= A[i] <= 109



Input Format
First and only argument is an integer array A of size N.



Output Format
Return an integer denoting the first repeating element.
"""


def solve(self, A):
        d = {}
        index = {}
        for i in range(len(A)):
            if A[i] not in d:
                d[A[i]] = 1
                index[A[i]] = i
            else:
                d[A[i]] += 1
        m = len(A)
        val = 0
        for ele in d:
            if d[ele] > 1:
                ind = index[ele]
                if ind < m:
                    m = ind
                    val = ele
        if m < len(A):
            return val
        return -1