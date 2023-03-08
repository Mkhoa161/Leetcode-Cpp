# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        track = []

        while head:
            track.append(head)
            head = head.next

        return track[len(track) // 2]
            

        

        
