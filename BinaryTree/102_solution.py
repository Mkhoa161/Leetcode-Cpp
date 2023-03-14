# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = [root]
        result = [[root.val]]

        while queue:
            level = []
            for i in range(len(queue)):
                curr_node = queue.pop(0)
                if curr_node.left:
                    level.append(curr_node.left.val)
                    queue.append(curr_node.left)
                if curr_node.right:
                    level.append(curr_node.right.val)
                    queue.append(curr_node.right)
            if level != []:
                result.append(level)
        return result
