"""
Given a singly linked list and an integer K, reverses the nodes of the

list K at a time and returns modified linked list.

NOTE : The length of the list is divisible by K

Example :

Given linked list 1 -> 2 -> 3 -> 4 -> 5 -> 6 and K=2,

You should return 2 -> 1 -> 4 -> 3 -> 6 -> 5
"""


def reverseList(self, A, B):
        if B==1:
            return A
        if A is None:
            return None
        cur=A
        main=A
        Prev=None
        x=0
        while x<B:
            temp=cur.next
            cur.next=Prev
            Prev=cur
            cur=temp
            x+=1
        main.next=self.reverseList(cur,B)
        return Prev