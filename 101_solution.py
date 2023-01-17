# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if (not p and q) or (not q and p):
            return False
        stack = [p]
        traverse = [q]

        while stack and traverse:
            x, y = stack.pop(0), traverse.pop(0)
            if x.val != y.val:
                return False
            if (x.left and not y.left) or (y.left and not x.left):
                return False
            if x.left and y.left:
                stack.append(x.left)
                traverse.append(y.left)
            if (x.right and not y.right) or (y.right and not x.right):
                return False
            if x.right and y.right:
                stack.append(x.right)
                traverse.append(y.right)
        return True

