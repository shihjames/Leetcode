# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
Time = O(n)
Space = O(n)
"""
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node_set = set()
        cur = head
        while cur:
            if cur in node_set:
                return cur
            else:
                node_set.add(cur)
                cur = cur.next
        return None