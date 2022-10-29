# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
Time = O(n)
Space = O(1)
"""
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prev_node = None
        while cur:
            next_node = cur.next
            cur.next = prev_node
            prev_node = cur
            cur = next_node
        return prev_node
            