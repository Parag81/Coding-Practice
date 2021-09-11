"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

Return 0 / 1 ( 0 for false, 1 for true ) for this problem
"""

def isValid(self, A):
        length = len(A)
        if length%2 != 0:
            return 0
        dict1 = {'(':')',
                '[':']',
                '{':'}',
                }
        ar = []
        for ele in A:
            if ele == '{' or ele == '[' or ele == '(':
                ar.append(ele)
            else:
                if len(ar) == 0:
                    return 0
                s = ar.pop()
                if dict1[s] != ele:
                    return 0
        if len(ar) > 0:
            return 0
        return 1