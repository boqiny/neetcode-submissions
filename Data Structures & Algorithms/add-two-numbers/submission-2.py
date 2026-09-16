# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        flag = 0
        head = ListNode()
        cur = head
        while l1 and l2:
            digit = l1.val + l2.val + flag
            flag = 0
            if digit >= 10:
                digit = digit % 10
                flag = 1
            cur.next = ListNode(digit)
            cur = cur.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            digit = l1.val + flag
            flag = 0
            if digit >= 10:
                digit = digit % 10
                flag = 1
            cur.next = ListNode(digit)
            cur = cur.next
            l1 = l1.next
        
        while l2:
            digit = l2.val + flag
            flag = 0
            if digit >= 10:
                digit = digit % 10
                flag = 1
            cur.next = ListNode(digit)
            cur = cur.next
            l2 = l2.next

        if flag:
            cur.next = ListNode(1)

        return head.next
            
            
            