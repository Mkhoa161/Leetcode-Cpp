# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 
        diameter = 0
        def height(node):
            nonlocal diameter
            if not node:
                return 0
            left_length = height(node.left)
            right_length = height(node.right)
            diameter = max(diameter, left_length + right_length)
            return 1 + max(left_length, right_length)
        height(root)
        return diameter

