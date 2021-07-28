"""
Given a matrix, A of size M x N of 0s and 1s. If an element is 0, set its entire row and column to 0.
Note: This will be evaluated on the extra memory used. Try to minimize the space and time complexity.

Input Format:

The first and the only argument of input contains a 2-d integer matrix, A, of size M x N.
Output Format:

Return a 2-d matrix that satisfies the given conditions.
Constraints:

1 <= N, M <= 1000
0 <= A[i][j] <= 1
Examples:

Input 1:
    [   [1, 0, 1],
        [1, 1, 1], 
        [1, 1, 1]   ]


Output 1:
    [   [0, 0, 0],
        [1, 0, 1],
        [1, 0, 1]   ]
"""

def setZeroes(self, A):
        lst = []
        il, jl = [], []
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 0:
                    lst.append([i, j])
        for i, j in lst:
            if i not in il:
                for j1 in range(len(A[0])):
                    A[i][j1] = 0
                il.append(i)
            if j not in jl:
                for i1 in range(len(A)):
                    A[i1][j] = 0
                jl.append(j)
        return A