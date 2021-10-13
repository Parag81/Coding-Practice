"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

"""

def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        list1,list2 = [],[]
        while l1 != None:
            list1.insert(0,str(l1.val))
            l1 = l1.next
        while l2 != None:
            list2.insert(0,str(l2.val))
            l2 = l2.next
        total = int("".join(list1)) + int("".join(list2))
        total = [int(x) for x in str(total)]
        l3 = None
        for i in range(0,len(total)):
            new = ListNode(total[i])
            new.next = l3
            l3 = new
        return l3
