class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    h = head
    count = 0
    while h:
        count += 1
        h = h.next
    dif = count - k
    if dif == 0:
        head = head.next
        return head
    h = head
    while dif > 1:
        dif -= 1
        h = h.next
    p = h.next
    h.next = p.next
    return head