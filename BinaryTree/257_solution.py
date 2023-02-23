# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(root):
            if not root:
                return 
            if not root.right and not root.left:
                track.append(str(root.val))
                res.append('->'.join(track))
                track.pop()
                return
            track.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
            track.pop()
        track = []
        res = []
        dfs(root)
        return res
