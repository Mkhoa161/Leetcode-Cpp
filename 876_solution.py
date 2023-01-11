# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        
        # Calculate the length of the linked list
        length = 1
        curr = head
        while curr.next is not None:
            length += 1
            curr = curr.next
        
        # Find the middle node
        res_node = head
        track = 1
        for i in range(length):
            if track == length//2 + 1:
                return res_node
            res_node = res_node.next
            track += 1
        
        
