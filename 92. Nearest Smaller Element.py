"""
Given an array, find the nearest smaller element G[i] for every element A[i] in the array such that the element has an index smaller than i.

More formally,

    G[i] for an element A[i] = an element A[j] such that 
    j is maximum possible AND 
    j < i AND
    A[j] < A[i]
Elements for which no smaller element exist, consider next smaller element as -1.

Input Format

The only argument given is integer array A.
Output Format

Return the integar array G such that G[i] contains nearest smaller number than A[i].If no such element occurs G[i] should be -1.
"""


def prevSmaller(self, A):
        res = [-1] * len(A)
        stack = []

        for i in range(len(A)-1, -1, -1):
            while stack and A[i] < A[stack[-1]]:
                res[stack.pop()] = A[i]
            stack.append(i)

        return res