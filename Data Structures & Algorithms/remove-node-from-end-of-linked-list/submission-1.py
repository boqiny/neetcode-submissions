# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        before = dummy
        length = 0
        while head:
            head = head.next
            length += 1
        remove_idx = length - n
        head = dummy.next
        for _ in range(remove_idx):
            before = head
            head = head.next
        before.next = head.next
        return dummy.next
