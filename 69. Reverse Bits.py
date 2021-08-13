"""
Problem Description

Reverse the bits of an 32 bit unsigned integer A.



Problem Constraints
0 <= A <= 232



Input Format
First and only argument of input contains an integer A.



Output Format
Return a single unsigned integer denoting the decimal value of reversed bits.
"""


def reverse(self, A):
        total = 0
        bit = 1
        A = bin(A)
        A = A[2:]
        length = len(A)
        st = ""
        for i in range(32-length):
            st += "0"
        A = st + A
        for ele in A:
            if ele == "1":
                total += bit
            bit *= 2
        return total