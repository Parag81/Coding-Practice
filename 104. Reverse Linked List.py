def reverse(self, head):
    if head.next is None:
        return head
    a = head
    b = head.next
    c = b.next
    a.next = None
    while c:
        b.next = a
        a = b
        b = c
        c = c.next
    b.next = a
    return b