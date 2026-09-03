# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        queue = deque([root])
        p_val = min(p.val, q.val)
        q_val = max(p.val, q.val)
        while queue:
            cur = queue.popleft()
            if p_val <= cur.val <= q_val:
                return cur
            elif cur.val < p.val:
                queue.append(cur.right)
            else:
                queue.append(cur.left)