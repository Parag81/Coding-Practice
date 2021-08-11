"""
Given a string A consisting only of lowercase characters, we need to check whether it is possible to make this string a palindrome after removing exactly one character from this.

If it is possible then return 1 else return 0.
"""


def solve(self, A):
        i, j = 0, len(A)-1
        count = 0
        while i <= j:
            if A[i] == A[j]:
                i += 1
                j -=1
            else:
                i += 1
                count += 1
        if count > 1:
            return 0
        return 1