# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
Time = O(max(m, n))
Space = O(max(m, n))
"""
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = cur = ListNode()
        carry = 0
        while l1 or l2:
            if l1:
                val1 = l1.val
                l1 = l1.next
            else:
                val1 = 0
            if l2:
                val2 = l2.val
                l2 = l2.next
            else:
                val2 = 0
            cur_sum = val1 + val2 + carry
            cur.next = ListNode(cur_sum % 10)
            carry = cur_sum // 10
            cur = cur.next 
            
        if carry != 0:
            cur.next = ListNode(carry)
            
        return dummy.next