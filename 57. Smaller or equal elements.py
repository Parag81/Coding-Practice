"""
Given an sorted array A of size N. Find number of elements which are less than or equal to B.

NOTE: Expected Time Complexity O(log N)



Problem Constraints
1 <= N <= 106

1 <= A[i], B <= 109



Input Format
First agument is an integer array A of size N.

Second argument is an integer B.



Output Format
Return an integer denoting the number of elements which are less than or equal to B.



Example Input
Input 1:

 A = [1, 3, 4, 4, 6]
 B = 4
Input 2:

 A = [1, 2, 5, 5]
 B = 3


Example Output
Output 1:

 4
Output 2:

 2
"""


def solve(self, A, B):
        if len(A) == 1:
            return 0
        i, j = 0, len(A)-1
        while i <= j:
            mid = (i + j)//2
            if mid < len(A)-1:
                if A[mid] == B and A[mid+1] != B:
                    return mid + 1
                elif A[mid] < B < A[mid + 1]:
                    return mid + 1
                elif A[mid] < B or (A[mid] == B and A[mid+1] == B):
                    i = mid + 1
                else:
                    j = mid - 1
            else:
                return len(A)