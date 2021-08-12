"""
Given an integer A, count and return the number of trailing zeroes.



Problem Constraints
1 <= A <= 109



Input Format
First and only argument is an integer A.



Output Format
Return an integer denoting the count of trailing zeroes.
"""


def solve(self, A):
        binary = bin(A)
        count = 0
        for i in reversed(binary):
            if i != "0":
                break
            count += 1
        return count