# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        def isSym(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            return left.val == right.val and isSym(left.right, right.left) and isSym(left.left, right.right)
        
        return isSym(root.left, root.right)
