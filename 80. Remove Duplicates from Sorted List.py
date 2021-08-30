"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,

Given 1->1->2, return 1->2.

Given 1->1->2->3->3, return 1->2->3.
"""


def deleteDuplicates(self, A):
        h = A
        while A:
            while A.next and A.val == A.next.val:
                A.next = A.next.next
            A = A.next
        return h