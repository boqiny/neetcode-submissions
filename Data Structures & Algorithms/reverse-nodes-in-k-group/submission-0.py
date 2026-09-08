# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        before = dummy
        while True:
            # 探路 k 个，不够就 break
            cur = head
            for _ in range(k):
                if cur:
                    cur = cur.next
                else:
                    return dummy.next

            prev = None
            flag = head

            # 反转 k 次
            for _ in range(k):
                temp = head.next
                head.next = prev
                prev = head
                head = temp
            
            before.next = prev
            flag.next = head
            before = flag
        