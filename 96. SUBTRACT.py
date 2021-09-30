"""
Given a singly linked list, modify the value of first half nodes such that :

1st node’s new value = the last node’s value - first node’s current value
2nd node’s new value = the second last node’s value - 2nd node’s current value,
and so on …

NOTE :

If the length L of linked list is odd, then the first half implies at first floor(L/2) nodes. So, if L = 5, the first half refers to first 2 nodes.
If the length L of linked list is even, then the first half implies at first L/2 nodes. So, if L = 4, the first half refers to first 2 nodes.
"""


def subtract(self, A):
        lst = []
        while A:
            lst.append(A.val)
            A = A.next
        i, j = 0, len(lst)-1
        while i < j:
            lst[i] = lst[j] - lst[i]
            i += 1
            j -= 1
        head = ListNode("/")
        ptr = head
        for ele in lst:
            node = ListNode(ele)
            ptr.next = node
            ptr = ptr.next
        return head.next