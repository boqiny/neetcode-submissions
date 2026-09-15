# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.vals = []
        self.i = -1

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            self.vals.append(node.val)
            inorder(node.right)
        inorder(root)

    def next(self) -> int:
        self.i += 1
        return self.vals[self.i]
        
    def hasNext(self) -> bool:
        return self.i + 1 < len(self.vals)
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()