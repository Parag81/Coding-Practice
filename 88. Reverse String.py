"""
Given a string S, reverse the string using stack.

Example :

Input : "abc"
Return "cba"
"""


def reverseString(self, A):
        ar = []
        for ele in A:
            ar.append(ele)
        string = ""
        while len(ar) > 0:
            string += ar.pop()
        return string