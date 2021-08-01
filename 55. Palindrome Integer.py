"""
Determine whether an integer is a palindrome. Do this without extra space.

A palindrome integer is an integer x for which reverse(x) = x where reverse(x) is x with its digit reversed. Negative numbers are not palindromic.

Example :

Input : 12121
Output : True


Input : 123
Output : False
"""

def isPalindrome(self, A):
        if A < 0:
            return 0
        lst = list(int(x) for x in str(A))
        l = len(lst)
        if l % 2 == 0:
            j = l // 2
            i = j - 1
        else:
            j = (l // 2) + 1
            i = (l // 2) - 1
        while i > -1:
            if lst[i] != lst[j]:
                return 0
            i -= 1
            j += 1
        return 1