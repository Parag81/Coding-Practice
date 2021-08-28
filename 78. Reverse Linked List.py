"""
Reverse a linked list. Do it in-place and in one-pass.

For example:

Given 1->2->3->4->5->NULL,

return 5->4->3->2->1->NULL.
"""


def reverseList(self, A):
        prev = None
        cur = A
        nextptr = None
        while cur:
            nextptr = cur.next
            cur.next = prev
            prev = cur
            cur = nextptr
        return prev