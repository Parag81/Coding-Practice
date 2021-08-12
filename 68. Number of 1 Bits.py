"""
Write a function that takes an integer and returns the number of 1 bits it has.


Problem Constraints
1 <= A <= 109


Input Format
First and only argument contains integer A


Output Format
Return an integer as the answer
"""


def numSetBits(self, A):
        binary = bin(A)
        return binary.count("1")