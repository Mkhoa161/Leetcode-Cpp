# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        if head is None:
            return None
        
        curr = head
        lst = [curr.val]
        while curr.next is not None:
            lst.append(curr.next.val)
            curr = curr.next
        
        lst = lst[::-1]
        power = 0
        res = 0
        for value in lst:
            if value == 1:
                res = res + 2 ** power
            power += 1
        return res
        
