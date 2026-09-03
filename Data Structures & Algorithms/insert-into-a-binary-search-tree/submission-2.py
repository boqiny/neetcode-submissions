# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        cur = root
        prev = cur
        while cur:
            if cur.val < val:
                prev = cur
                cur = cur.right
            else:
                prev = cur
                cur = cur.left
        cur = TreeNode(val)
        if val < prev.val:
            prev.left = cur
        else:
            prev.right = cur
        return root
        

            
        