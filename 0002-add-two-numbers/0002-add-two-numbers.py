# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = cur = ListNode()
        carry = 0
        while l1 and l2:
            cur_sum = l1.val + l2.val + carry
            cur.next = ListNode(cur_sum % 10)
            carry = cur_sum // 10
            cur = cur.next
            l1 = l1.next 
            l2 = l2.next
        if l1:
            while l1:
                cur_sum = l1.val + carry
                cur.next = ListNode(cur_sum % 10)
                carry = cur_sum // 10
                cur = cur.next
                l1 = l1.next 
        else:
            while l2:
                cur_sum = l2.val + carry
                cur.next = ListNode(cur_sum % 10)
                carry = cur_sum // 10
                cur = cur.next
                l2 = l2.next 
            
        if carry != 0:
            cur.next = ListNode(carry)
        return dummy.next