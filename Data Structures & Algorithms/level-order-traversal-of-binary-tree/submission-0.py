# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque([(root,0)])
        cur_depth = 0
        subset = []
        res = []
        while q:
            cur_node, depth = q.popleft()
            if cur_depth != depth:
                res.append(subset)
                subset = []
                cur_depth = depth
            subset.append(cur_node.val)
            if cur_node.left:
                q.append((cur_node.left, depth+1))
            if cur_node.right:
                q.append((cur_node.right, depth+1))
        res.append(subset)
        return res

            
            

        