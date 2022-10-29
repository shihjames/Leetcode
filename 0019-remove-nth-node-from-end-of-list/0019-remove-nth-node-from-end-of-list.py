# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        length -= n
        cur = dummy
        while length > 0:
            length -= 1
            cur = cur.next
        cur.next = cur.next.next
        return dummy.next