# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        idx = 1
        prev = None
        dummy = ListNode(0,head)
        before = dummy

        while idx < left:
            idx += 1
            before = head
            head = head.next

        flag = head

        while idx <= right:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
            idx += 1
        flag.next = head
        before.next = prev
        return dummy.next


