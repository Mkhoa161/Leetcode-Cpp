# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        sum = 0
        def dfs_findtotal(node):    
            nonlocal sum
            if not node:
                return 0
            left_total = dfs_findtotal(node.left)
            right_total = dfs_findtotal(node.right)
            tilt = abs(left_total - right_total)
            sum += tilt
            return node.val + left_total + right_total
        dfs_findtotal(root)
        return sum
