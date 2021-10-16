"""
Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.

 

Example 1:

Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.
"""

def countNegatives(self, grid):
        total = 0
        for i in range(len(grid)):
            for j in reversed(grid[i]):
                if j >= 0:
                    break
                total += 1
        return total
