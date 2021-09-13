"""
Given a string A consisting only of '(' and ')'.

You need to find whether parantheses in A is balanced or not ,if it is balanced then return 1 else return 0.
"""


def solve(self, A):
        ar = []
        for ele in A:
            if ele == "(":
                ar.append(ele)
            else:
                if len(ar) == 0:
                    return 0
                ar.pop()
        if len(ar) > 0:
            return 0
        return 1