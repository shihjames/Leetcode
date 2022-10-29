# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        cur = head
        target_node = None
        while cur:
            length += 1
            cur = cur.next
        if length == n:
            return head.next
        count = 0
        cur = head
        while cur:
            count += 1
            if count == length-n:
                cur.next = cur.next.next
            cur = cur.next
        return head