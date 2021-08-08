"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Example:

"A man, a plan, a canal: Panama" is a palindrome.

"race a car" is not a palindrome.

Return 0 / 1 ( 0 for false, 1 for true ) for this problem
"""


def isPalindrome(self, A):
        A = "".join(char for char in A if char.isalnum())
        A = A.lower()
        length = len(A)
        if len(A) % 2 == 0:
            i = length//2 - 1
            j = length//2
        else:
            i = length // 2 - 1
            j = length // 2 + 1
        while i > -1:
            if A[i] != A[j]:
                return 0
            i -= 1
            j += 1
        return 1