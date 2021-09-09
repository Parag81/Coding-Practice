"""
Given a linked list, swap every two adjacent nodes and return its head.

For example,

Given 1->2->3->4, you should return the list as 2->1->4->3.
"""


def swapPairs(self, A):
        h = A
        while h is not None and h.next is not None:
            h.val, h.next.val = h.next.val, h.val
            h = h.next.next
        return A