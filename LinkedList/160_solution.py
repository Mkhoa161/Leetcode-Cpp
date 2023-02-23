# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # concatenate headA and headB
        if not headA or not headB:
            return None
        last = headA
        while last.next is not None:
            last = last.next
        last.next = headB

        # if headA and headB intersect, there will be a cycle in the concatenated version
        # find the start of the cycle which is the node of intersection
        slow = fast = headA
        while fast and fast.next:            
            slow, fast = slow.next, fast.next.next
            if slow is fast:
                fast = headA
                while fast is not slow:
                    fast, slow = fast.next, slow.next
                last.next = None # seperate headA and headB so that they are not modified
                return slow
        else:
            last.next = None # seperate headA and headB so that they are not modified
            return None
        
