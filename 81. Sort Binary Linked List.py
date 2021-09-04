"""
Problem Description

Given a Linked List A consisting of N nodes.

The Linked List is binary i.e data values in the linked list nodes consist of only 0's and 1's.

You need to sort the linked list and return the new linked list.

NOTE:

Try to do it in constant space.
"""


def solve(self, A):
        head = A
        n = A
        count0 = 0
        count1 = 0
        while n:
            if n.val == 0:
                count0 += 1
            else:
                count1 += 1
            n = n.next
        count1 += count0
        count = 0
        while count1 > 0:
            if count < count0:
                A.val = 0
                count1 -= 1
                count += 1
            else:
                A.val = 1
                count1 -= 1
            A = A.next
        return head