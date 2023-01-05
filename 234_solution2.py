# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        self.front = head
        def check_Palindrome(curr_node = head):
            if curr_node is not None:
                if not check_Palindrome(curr_node.next):
                    return False
                if self.front.val != curr_node.val:
                    return False
                self.front = self.front.next
            return True
        return check_Palindrome() 

