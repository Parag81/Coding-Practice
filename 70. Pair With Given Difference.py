"""
Given an one-dimensional unsorted array A containing N integers.

You are also given an integer B, find if there exists a pair of elements in the array whose difference is B.

Return 1 if any such pair exists else return 0.
"""


def solve(self, A, B):
        A.sort()
        for i in range(len(A)):
            for j in range(len(A)-1, i, -1):
                if abs(A[i] - A[j]) == abs(B):
                    return 1
                if A[i] - A[j] > B:
                    break
        return 0