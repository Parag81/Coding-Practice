"""
Problem Description

Given a linked list A of length N and an integer B.

You need to find the value of the Bth node from the middle towards the beginning of the Linked List A.

If no such element exists, then return -1.

NOTE:

Position of middle node is: (N/2)+1, where N is the total number of nodes in the list.
"""

# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        h = A
        count = 0
        while h:
            count += 1
            h = h.next
        mid = (count//2)+1
        dif = mid - B
        if dif <= 0:
            return -1
        while dif > 0:
            value = A.val
            A = A.next
            dif -= 1
	return value