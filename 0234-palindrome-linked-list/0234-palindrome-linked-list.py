# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverse(node):
            prev, cur = None, node
            while cur:
                next_node = cur.next
                cur.next = prev
                prev = cur
                cur = next_node
            return  prev
        
        if not head and not head.next:
            return True
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        tail = reverse(slow)
        while head and tail:
            if head.val != tail.val:
                return False
            head, tail = head.next, tail.next
        return True
        
        
    