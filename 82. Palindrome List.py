"""
Given a singly linked list, determine if its a palindrome. Return 1 or 0 denoting if its a palindrome or not, respectively.

Notes:

Expected solution is linear in time and constant in space.
For example,

List 1-->2-->1 is a palindrome.
List 1-->2-->3 is not a palindrome.
"""

def lPalin(self, A):
        lst = []
        while A:
            lst.append(A.val)
            A = A.next
        i, j = 0, len(lst)-1
        while i <= j:
            if lst[i] != lst[j]:
                return 0
            else:
                i += 1
                j -= 1
        return 1