"""
Given an integer n, return any array containing n unique integers such that they add up to 0.

 

Example 1:

Input: n = 5
Output: [-7,-1,1,3,4]
Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].
"""

def sumZero(self, n):
        lst = []
        if n == 1:
            return [0]
        m = n
        for i in range(n//2):
            lst.append(m)
            lst.append(-m)
            m -= 1
        if n % 2 != 0:
            lst.append(0)
        return lst