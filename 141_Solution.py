# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is not None:
            curr_node = head
            curr_node.val = None
            while curr_node.next is not None:
                if curr_node.next.val == None:
                    return True
                curr_node.next.val = None
                curr_node = curr_node.next
            return False
        else:
            return False
