# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return None
        lst = []
        def track(root):
            if root:
                lst.append(root.val)
                if root.left:
                    track(root.left)
                if root.right:
                    track(root.right)           
        track(root)
        return lst
