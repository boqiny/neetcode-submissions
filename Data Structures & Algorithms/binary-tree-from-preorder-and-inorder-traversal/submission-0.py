# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#         1
#        / \
#       2   3
#      / \   \
#     4   5   6

# preorder = [1, 2, 4, 5, 3, 6]
# inorder  = [4, 2, 5, 1, 3, 6]

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx = {val: i for i, val in enumerate(inorder)}
        i = 0

        def dfs(l, r):
            nonlocal i
            if l > r:
                return None
            root_val = preorder[i]
            i += 1
            mid = idx[root_val]
            root = TreeNode(root_val)
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)
            return root
        return dfs(0, len(preorder)-1)