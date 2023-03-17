# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None

        queue = [root]
        while queue:
            node = queue.pop(0)
            if node.val == val:
                return node
            if node.left and val < node.val:
                queue.append(node.left)
            elif node.right and node.val < val:
                queue.append(node.right)
        return None
