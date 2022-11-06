# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        carry = 0
        
        while l1 is not None or l2 is not None:
            if l1:
                l1_val = l1.val
                l1 = l1.next
            else:
                l1_val = 0
            
            if l2:
                l2_val = l2.val
                l2 = l2.next
            else:
                l2_val = 0
                
            cur_sum = l1_val + l2_val + carry
            new_val = cur_sum % 10
            carry = cur_sum // 10
            
            cur.next = ListNode(new_val)
            cur = cur.next
        
        if carry != 0:
            cur.next = ListNode(carry)
        
        return dummy.next