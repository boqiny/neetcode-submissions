# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')

        def dfs(node) -> int:
            nonlocal max_sum
            if not node:
                return float('-inf')
            left = dfs(node.left)
            right = dfs(node.right)
            cur_max = max(node.val, node.val + left, node.val + right, node.val + left + right)
            max_sum = max(max_sum, cur_max)
            return max(node.val, node.val + left, node.val + right)

        dfs(root)
        return max_sum
            
            

