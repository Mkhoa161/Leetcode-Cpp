# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        lst = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            lst.append(node.val)
            dfs(node.right)
        dfs(root)
        dummy = curr = TreeNode(None)
        for i in range(len(lst)):
            curr.right = TreeNode(lst[i])
            curr = curr.right
        return dummy.right
