# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root, sum):
            if not root:
                return False

            sum += root.val

            if sum == targetSum and not root.left and not root.right:
                return True

            return dfs(root.right, sum) or dfs(root.left, sum)
        
        return dfs(root, 0)
                
