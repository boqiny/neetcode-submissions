# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # dfs using stack
        if not root:
            return 0
        stack = [(root, 1)]
        max_depth = 0
        while stack:
            cur_node, depth = stack.pop()
            max_depth = max(max_depth, depth)
            if cur_node.left:
                stack.append((cur_node.left, depth + 1))
            if cur_node.right:
                stack.append((cur_node.right, depth + 1))
        return max_depth
