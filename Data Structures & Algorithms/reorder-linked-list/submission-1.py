# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        q = deque()
        cur = head
        while cur:
            q.append(cur)
            cur = cur.next
        dummy = ListNode()
        cur = dummy

        while q:
            cur.next = q.popleft()
            cur = cur.next
            if q:
                cur.next = q.pop()
                cur = cur.next
        
        cur.next = None
