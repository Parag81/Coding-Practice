"""
Given a bitonic sequence A of N distinct elements, write a program to find a given element B in the bitonic sequence in O(logN) time.

NOTE:

A Bitonic Sequence is a sequence of numbers which is first strictly increasing then after a point strictly decreasing.


Problem Constraints
3 <= N <= 105

1 <= A[i], B <= 108

Given array always contain a bitonic point.

Array A always contain distinct elements.



Input Format
First argument is an integer array A denoting the bitonic sequence.

Second argument is an integer B.



Output Format
Return a single integer denoting the position (0 index based) of the element B in the array A if B doesn't exist in A return -1.
"""


def findMax(A, B):
    i, j = 0, len(A) - 1
    while i <= j:
        mid = (i + j) // 2
        if A[mid - 1] < A[mid] > A[mid + 1]:
            return mid
        elif A[mid - 1] < A[mid] < A[mid + 1]:
            i = mid + 1
        else:
            j = mid - 1

def search(A, B, ind, flag):
    if flag == 0:
        i, j = 0, ind
        while i <= j:
            mid = (i + j) // 2
            if A[mid] == B:
                return mid
            elif A[mid] < B:
                i = mid + 1
            else:
                j = mid - 1
        return -1
    else:
        i, j = ind, len(A)-1
        while i <= j:
            mid = (i + j) // 2
            if A[mid] == B:
                return mid
            elif A[mid] > B:
                i = mid + 1
            else:
                j = mid - 1
    return -1


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        ind = findMax(A, B)
        if A[ind] == B:
            return ind
        left_search = search(A, B, ind, 0)
        if left_search != -1:
            return left_search
        right_search = search(A, B, ind, 1)
        if right_search != -1:
            return right_search
        return -1