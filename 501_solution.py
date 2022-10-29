# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
            if not root:
                return None
            stack = [root]
            count = {root.val : 1}
            while stack:
                node = stack.pop()
                if node.left:
                    stack.append(node.left)
                    if node.left.val not in count:
                        count.update({node.left.val : 1})
                    elif node.left.val in count:
                        count[node.left.val] += 1
                if node.right:
                    stack.append(node.right)
                    if node.right.val not in count:
                        count.update({node.right.val : 1})
                    elif node.right.val in count:
                        count[node.right.val] += 1
            max_value = 0
            for key in count:
                if count[key] >= max_value:
                    max_value = count[key] 
            lst = []
            for key in count:
                if count[key] == max_value:
                    lst.append(key)
            return lst
            

            
