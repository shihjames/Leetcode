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
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = cur1 = ListNode()
        even = cur2 = ListNode()
        count = 1
        while head:
            if count % 2 == 1:
                cur1.next = head
                cur1 = cur1.next
            else:
                cur2.next = head
                cur2 = cur2.next
            head = head.next
            count += 1
        
        cur2.next = None
        cur1.next = even.next
        return odd.next
        
            