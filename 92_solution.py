# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        curr_node = head
        track = 1
        val_list = []
        while curr_node is not None:
            if left == track:
                val_list.append(curr_node.val)
                while curr_node is not None:
                    if right == track:
                        val_list.reverse()
                        curr = head
                        pos = 1
                        while curr is not None:
                            if left == pos:   
                                for val in val_list:
                                    curr.val = val
                                    curr = curr.next
                                return head
                            else:
                                curr = curr.next
                                pos += 1    
                    val_list.append(curr_node.next.val)
                    curr_node = curr_node.next 
                    track += 1
            curr_node = curr_node.next
            track += 1
